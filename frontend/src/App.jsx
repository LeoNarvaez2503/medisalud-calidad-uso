import React, { useState, useEffect } from 'react';
import { 
  Activity, 
  AlertOctagon, 
  Smartphone, 
  User, 
  Database, 
  CheckCircle, 
  Clock, 
  CreditCard, 
  PhoneCall, 
  FileText, 
  RefreshCw, 
  Tablet, 
  AlertTriangle, 
  Cpu 
} from 'lucide-react';

const API_BASE = '/api'; // Routed via Nginx proxy

export default function App() {
  // Global States
  const [pacientes, setPacientes] = useState([]);
  const [selectedPacienteId, setSelectedPacienteId] = useState('');
  const [selectedPaciente, setSelectedPaciente] = useState(null);
  const [auditLogs, setAuditLogs] = useState([]);
  const [auditStats, setAuditStats] = useState({
    total_incidentes: 0,
    caracteristicas: {},
    modulos: {},
    violaciones_rnf: 0
  });

  // HCE States
  const [alergias, setAlergias] = useState('');
  const [alergiaError, setAlergiaError] = useState(false);
  const [simulateAlergiaError, setSimulateAlergiaError] = useState(false);
  
  const [diagnostico, setDiagnostico] = useState('');
  const [notaEvolucion, setNotaEvolucion] = useState('');
  const [savingNota, setSavingNota] = useState(false);
  const [notaSuccessMessage, setNotaSuccessMessage] = useState(null);
  const [simulateNotaDelay, setSimulateNotaDelay] = useState(false);

  const [medicamento, setMedicamento] = useState('');
  const [dosis, setDosis] = useState('');
  const [indicaciones, setIndicaciones] = useState('');
  const [recetaResult, setRecetaResult] = useState(null);
  const [simulateDosisError, setSimulateDosisError] = useState(false);

  // Portal Citas States
  const [bookingStep, setBookingStep] = useState(1);
  const [bookingIntentos, setBookingIntentos] = useState(1);
  const [bookingStatus, setBookingStatus] = useState(null);
  const [bookingConflict, setBookingConflict] = useState(false);
  const [simulateBookingError, setSimulateBookingError] = useState(false);

  // Facturacion States
  const [pagoStatus, setPagoStatus] = useState(null);
  const [reintentoPago, setReintentoPago] = useState(false);
  const [simulatePagoDelay, setSimulatePagoDelay] = useState(false);

  // Telemedicina States
  const [telemedicinaActive, setTelemedicinaActive] = useState(false);
  const [telemedicinaStatus, setTelemedicinaStatus] = useState(null);
  const [telemedicinaStreamError, setTelemedicinaStreamError] = useState(false);
  const [simulateTelemedicinaError, setSimulateTelemedicinaError] = useState(false);

  // Selected Log Detail for Modal
  const [selectedLog, setSelectedLog] = useState(null);

  // Load patient list and initial stats
  useEffect(() => {
    fetchPacientes();
    fetchAuditData();
    const interval = setInterval(fetchAuditData, 3000); // Polling logs every 3s
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (selectedPacienteId) {
      const pac = pacientes.find(p => p.id === parseInt(selectedPacienteId));
      setSelectedPaciente(pac);
      setAlergias('');
      setAlergiaError(false);
    } else {
      setSelectedPaciente(null);
    }
  }, [selectedPacienteId, pacientes]);

  const fetchPacientes = async () => {
    try {
      const res = await fetch(`${API_BASE}/pacientes`);
      if (res.ok) {
        const data = await res.json();
        setPacientes(data);
        if (data.length > 0) setSelectedPacienteId(data[0].id.toString());
      }
    } catch (err) {
      console.error("Error fetching patients", err);
    }
  };

  const fetchAuditData = async () => {
    try {
      const resLogs = await fetch(`${API_BASE}/auditoria/logs`);
      const resStats = await fetch(`${API_BASE}/auditoria/stats`);
      if (resLogs.ok && resStats.ok) {
        setAuditLogs(await resLogs.json());
        setAuditStats(await resStats.json());
      }
    } catch (err) {
      console.error("Error fetching audit logs", err);
    }
  };

  // Actions
  const handleLoadAlergias = async () => {
    if (!selectedPacienteId) return;
    try {
      const res = await fetch(
        `${API_BASE}/pacientes/${selectedPacienteId}/alergias?simulate_error=${simulateAlergiaError}&rol_usuario=Medico&sede=Quito`
      );
      const data = await res.json();
      if (data.error) {
        setAlergias("ERROR AL CARGAR HISTORIAL CLÍNICO");
        setAlergiaError(true);
      } else {
        setAlergias(data.alergias);
        setAlergiaError(false);
      }
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleSaveNota = async (e) => {
    e.preventDefault();
    if (!selectedPacienteId || !notaEvolucion) return;
    setSavingNota(true);
    setNotaSuccessMessage(null);
    try {
      const res = await fetch(`${API_BASE}/hce/nota?simulate_error=${simulateNotaDelay}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          paciente_id: parseInt(selectedPacienteId),
          diagnostico,
          nota_evolucion: notaEvolucion,
          rol_usuario: 'Medico',
          sede: 'Quito'
        })
      });
      const data = await res.json();
      setSavingNota(false);
      setNotaSuccessMessage(data);
      setNotaEvolucion('');
      setDiagnostico('');
      fetchAuditData();
    } catch (err) {
      setSavingNota(false);
      console.error(err);
    }
  };

  const handleSaveReceta = async (e) => {
    e.preventDefault();
    if (!selectedPacienteId || !medicamento || !dosis) return;
    try {
      const res = await fetch(`${API_BASE}/hce/receta?simulate_error=${simulateDosisError}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          paciente_id: parseInt(selectedPacienteId),
          medicamento,
          dosis,
          indicaciones,
          rol_usuario: 'Medico',
          sede: 'Quito'
        })
      });
      const data = await res.json();
      setRecetaResult(data);
      setMedicamento('');
      setDosis('');
      setIndicaciones('');
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  // Mobile App Simulation Actions
  const handleBookingNext = () => {
    if (bookingStep < 5) {
      setBookingStep(bookingStep + 1);
    }
  };

  const handleConfirmCita = async () => {
    if (!selectedPacienteId) return;
    
    if (simulateBookingError && bookingIntentos < 4) {
      // Simulates confusion/abandonment error
      try {
        await fetch(`${API_BASE}/citas/agendar?simulate_error=true`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            paciente_id: parseInt(selectedPacienteId),
            especialidad: 'Cardiología',
            medico: 'Dr. Alejandro Tobar',
            fecha_hora: '2026-07-20 09:00',
            rol_usuario: 'Paciente',
            sede: 'Quito',
            intentos: bookingIntentos
          })
        });
        setBookingIntentos(bookingIntentos + 1);
        setBookingStatus({ status: "Sesión expirada antes del paso de confirmación. Reintente.", error: true });
        setBookingStep(1); // Force return to step 1
        fetchAuditData();
      } catch (err) {
        console.error(err);
      }
      return;
    }

    // Success (or conflict if error simulate was active and attempts reached 4)
    try {
      const res = await fetch(`${API_BASE}/citas/agendar?simulate_error=${simulateBookingError}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          paciente_id: parseInt(selectedPacienteId),
          especialidad: 'Cardiología',
          medico: 'Dr. Alejandro Tobar',
          fecha_hora: '2026-07-20 09:00',
          rol_usuario: 'Paciente',
          sede: 'Quito',
          intentos: bookingIntentos
        })
      });
      const data = await res.json();
      setBookingStatus(data);
      if (data.error_duplicidad) {
        setBookingConflict(true);
      } else {
        setBookingConflict(false);
      }
      setBookingStep(5); // Complete
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleResetCitasSim = () => {
    setBookingStep(1);
    setBookingIntentos(1);
    setBookingStatus(null);
    setBookingConflict(false);
  };

  const handleProcesarPago = async () => {
    if (!selectedPacienteId) return;
    setPagoStatus({ status: "Procesando pago con pasarela...", loading: true });
    try {
      const res = await fetch(`${API_BASE}/facturacion/pagar?simulate_error=${simulatePagoDelay}&reintento=${reintentoPago}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          paciente_id: parseInt(selectedPacienteId),
          monto: 45.0,
          tarjeta: '4111 XXXX XXXX 1111',
          reintento: reintentoPago,
          rol_usuario: 'Paciente',
          sede: 'Quito'
        })
      });
      const data = await res.json();
      setPagoStatus(data);
      if (data.reintento_requerido) {
        setReintentoPago(true);
      } else {
        setReintentoPago(false);
      }
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleStartTelemedicina = async () => {
    if (!selectedPacienteId) return;
    setTelemedicinaActive(true);
    setTelemedicinaStatus("Iniciando llamada...");
    setTelemedicinaStreamError(false);
    
    try {
      const res = await fetch(`${API_BASE}/telemedicina/iniciar?simulate_error=${simulateTelemedicinaError}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          paciente_id: parseInt(selectedPacienteId),
          medico: 'Dra. Elena Rossi',
          rol_usuario: 'Paciente',
          sede: 'Quito'
        })
      });
      const data = await res.json();
      
      if (data.error_conexion) {
        setTelemedicinaStatus("Llamada en curso (Conexión inestable)...");
        // Trigger call cut simulator
        setTimeout(() => {
          setTelemedicinaStreamError(true);
          setTelemedicinaStatus("Llamada finalizada abruptamente (RNF-05 Incumplido)");
        }, 5000);
      } else {
        setTelemedicinaStatus("Conexión Estable - Consulta en curso.");
      }
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleMobileContextError = async () => {
    try {
      await fetch(`${API_BASE}/auditoria/contexto?modulo=Portal Citas&error_type=mobile&rol=Paciente&sede=Ambato`, { method: 'POST' });
      alert("Simulación de error Contexto Móvil enviada al Auditor.");
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleTabletContextError = async () => {
    try {
      await fetch(`${API_BASE}/auditoria/contexto?modulo=HCE&error_type=tablet&rol=Enfermeria&sede=Manta`, { method: 'POST' });
      alert("Simulación de error Contexto Tablet enviada al Auditor.");
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleLabIntegrationError = async () => {
    try {
      await fetch(`${API_BASE}/integraciones/orden?modulo=Laboratorio&tipo=Lab&simulate_error=true&rol=Enfermeria&sede=Quito`, { method: 'POST' });
      alert("Simulación de error de integración de Laboratorio (RabbitMQ) enviada al Auditor.");
      fetchAuditData();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="app-container">
      {/* Header Banner */}
      <header className="glass-panel" style={{ padding: '20px', marginBottom: '24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.8rem', fontWeight: 800, color: 'var(--primary)', letterSpacing: '-0.5px', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Activity size={28} /> MediSalud HIS
          </h1>
          <p style={{ margin: '5px 0 0 0', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
            Consola de Simulación y Auditoría de Calidad en Uso (ISO/IEC 25022)
          </p>
        </div>
        <div style={{ display: 'flex', gap: '15px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem' }}>
            <span style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: 'var(--success)' }}></span>
            <span>PostgreSQL: Conectado</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem' }}>
            <span style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: 'var(--warning)', boxShadow: '0 0 10px rgba(245,158,11,0.5)' }}></span>
            <span>RabbitMQ: Simulado</span>
          </div>
        </div>
      </header>

      {/* Global Context Selector */}
      <div className="glass-panel" style={{ padding: '15px', marginBottom: '24px', display: 'flex', alignItems: 'center', gap: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <User size={18} color="var(--primary)" />
          <span style={{ fontSize: '0.9rem', fontWeight: 600 }}>Seleccionar Paciente Activo:</span>
        </div>
        <select 
          value={selectedPacienteId}
          onChange={(e) => setSelectedPacienteId(e.target.value)}
          style={{ 
            backgroundColor: 'var(--bg-tertiary)', 
            color: 'var(--text-primary)', 
            border: '1px solid var(--border-color)', 
            borderRadius: '6px', 
            padding: '8px 12px',
            fontSize: '0.9rem',
            outline: 'none',
            cursor: 'pointer'
          }}
        >
          {pacientes.map(p => (
            <option key={p.id} value={p.id}>{p.nombre} ({p.historia_clinica})</option>
          ))}
        </select>
        {selectedPaciente && (
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Doc: {selectedPaciente.documento} | Alergias Registradas: <span style={{ color: 'var(--danger)', fontWeight: 600 }}>{selectedPaciente.alergias}</span>
          </div>
        )}
      </div>

      {/* Main Column Grid */}
      <div className="grid-3">
        
        {/* Column 1: HCE Clinical Portal */}
        <section className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '20px', borderBottom: '1px solid var(--border-color)', paddingBottom: '10px' }}>
            <FileText color="var(--primary)" />
            <h2 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 700 }}>1. HCE Portal Clínico (Médico)</h2>
          </div>

          {/* 1A. Allergy Check */}
          <div style={{ marginBottom: '24px', padding: '15px', backgroundColor: 'rgba(255,255,255,0.02)', borderRadius: '10px', border: '1px solid var(--border-color)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
              <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Verificar Historial de Alergias</span>
              <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', cursor: 'pointer', color: 'var(--text-secondary)' }}>
                <input 
                  type="checkbox" 
                  checked={simulateAlergiaError} 
                  onChange={(e) => setSimulateAlergiaError(e.target.checked)} 
                />
                Simular Falla de Carga
              </label>
            </div>
            <button className="btn btn-secondary" style={{ width: '100%', marginBottom: '10px' }} onClick={handleLoadAlergias}>
              Cargar Alergias en Pantalla
            </button>
            {alergias && (
              <div style={{ 
                padding: '10px', 
                borderRadius: '6px', 
                backgroundColor: alergiaError ? 'rgba(239,68,68,0.1)' : 'rgba(16,185,129,0.1)',
                border: `1px solid ${alergiaError ? 'var(--danger)' : 'var(--success)'}`,
                color: alergiaError ? 'var(--danger)' : 'var(--success)',
                fontSize: '0.85rem',
                fontWeight: 600
              }}>
                {alergias}
              </div>
            )}
          </div>

          {/* 1B. Save clinical Note */}
          <div style={{ marginBottom: '24px', padding: '15px', backgroundColor: 'rgba(255,255,255,0.02)', borderRadius: '10px', border: '1px solid var(--border-color)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Nota de Evolución Clínica</span>
              <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', cursor: 'pointer', color: 'var(--text-secondary)' }}>
                <input 
                  type="checkbox" 
                  checked={simulateNotaDelay} 
                  onChange={(e) => setSimulateNotaDelay(e.target.checked)} 
                />
                Simular Latencia (RNF-01)
              </label>
            </div>
            <form onSubmit={handleSaveNota}>
              <input 
                type="text" 
                placeholder="Diagnóstico CIE-10" 
                value={diagnostico}
                onChange={(e) => setDiagnostico(e.target.value)}
                style={{ 
                  width: '93%', 
                  backgroundColor: 'var(--bg-primary)', 
                  border: '1px solid var(--border-color)', 
                  borderRadius: '6px', 
                  padding: '8px 12px', 
                  color: 'white', 
                  marginBottom: '10px',
                  fontSize: '0.85rem'
                }}
              />
              <textarea 
                rows="3" 
                placeholder="Escriba la nota de evolución clínica..." 
                value={notaEvolucion}
                onChange={(e) => setNotaEvolucion(e.target.value)}
                required
                style={{ 
                  width: '93%', 
                  backgroundColor: 'var(--bg-primary)', 
                  border: '1px solid var(--border-color)', 
                  borderRadius: '6px', 
                  padding: '8px 12px', 
                  color: 'white', 
                  marginBottom: '12px',
                  fontSize: '0.85rem',
                  resize: 'none'
                }}
              />
              <button type="submit" disabled={savingNota} className="btn btn-primary" style={{ width: '100%' }}>
                {savingNota ? <><RefreshCw className="animate-spin" size={16} /> Guardando en Servidor...</> : "Guardar Nota"}
              </button>
            </form>

            {notaSuccessMessage && (
              <div style={{ 
                marginTop: '10px', 
                padding: '10px', 
                borderRadius: '6px', 
                backgroundColor: notaSuccessMessage.violacion_rnf ? 'rgba(245,158,11,0.1)' : 'rgba(16,185,129,0.1)',
                border: `1px solid ${notaSuccessMessage.violacion_rnf ? 'var(--warning)' : 'var(--success)'}`,
                fontSize: '0.8rem',
                color: notaSuccessMessage.violacion_rnf ? 'var(--warning)' : 'var(--success)'
              }}>
                <div style={{ fontWeight: 600 }}>{notaSuccessMessage.status}</div>
                <div>Tiempo de respuesta: {parseFloat(notaSuccessMessage.tiempo_segundos).toFixed(2)}s</div>
                {notaSuccessMessage.violacion_rnf && (
                  <div style={{ fontWeight: 700, marginTop: '4px' }}>⚠️ ALERTA: Latencia &gt; 8s. RNF-01 INCUMPLIDO</div>
                )}
              </div>
            )}
          </div>

          {/* 1C. Prescription */}
          <div style={{ padding: '15px', backgroundColor: 'rgba(255,255,255,0.02)', borderRadius: '10px', border: '1px solid var(--border-color)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Emitir Receta Electrónica</span>
              <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', cursor: 'pointer', color: 'var(--text-secondary)' }}>
                <input 
                  type="checkbox" 
                  checked={simulateDosisError} 
                  onChange={(e) => setSimulateDosisError(e.target.checked)} 
                />
                Simular Error de Dosis
              </label>
            </div>
            <form onSubmit={handleSaveReceta}>
              <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
                <input 
                  type="text" 
                  placeholder="Medicamento" 
                  value={medicamento}
                  onChange={(e) => setMedicamento(e.target.value)}
                  required
                  style={{ flex: 2, backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border-color)', borderRadius: '6px', padding: '8px 12px', color: 'white', fontSize: '0.85rem' }}
                />
                <input 
                  type="text" 
                  placeholder="Dosis (ej. 500 mg)" 
                  value={dosis}
                  onChange={(e) => setDosis(e.target.value)}
                  required
                  style={{ flex: 1, backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border-color)', borderRadius: '6px', padding: '8px 12px', color: 'white', fontSize: '0.85rem' }}
                />
              </div>
              <input 
                type="text" 
                placeholder="Indicaciones (ej. Cada 8 horas por 5 días)" 
                value={indicaciones}
                onChange={(e) => setIndicaciones(e.target.value)}
                style={{ width: '93%', backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border-color)', borderRadius: '6px', padding: '8px 12px', color: 'white', marginBottom: '10px', fontSize: '0.85rem' }}
              />
              <button type="submit" className="btn btn-secondary" style={{ width: '100%' }}>
                Generar Receta
              </button>
            </form>

            {recetaResult && (
              <div style={{ 
                marginTop: '10px', 
                padding: '10px', 
                borderRadius: '6px', 
                backgroundColor: recetaResult.error ? 'rgba(239,68,68,0.1)' : 'rgba(16,185,129,0.1)',
                border: `1px solid ${recetaResult.error ? 'var(--danger)' : 'var(--success)'}`,
                fontSize: '0.8rem'
              }}>
                <div style={{ fontWeight: 600 }}>Receta Emitida:</div>
                <div>Fármaco: {recetaResult.medicamento}</div>
                <div style={{ color: recetaResult.error ? 'var(--danger)' : 'white', fontWeight: recetaResult.error ? 700 : 400 }}>
                  Dosis Guardada: {recetaResult.dosis}
                </div>
                {recetaResult.error && (
                  <div style={{ fontWeight: 700, marginTop: '4px', color: 'var(--danger)' }}>🚨 ERROR CLÍNICO: DOSIS ALTERADA (Riesgo Salud)</div>
                )}
              </div>
            )}
          </div>
        </section>

        {/* Column 2: Portal del Paciente (Móvil Simulado) */}
        <section className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '20px', borderBottom: '1px solid var(--border-color)', paddingBottom: '10px' }}>
            <Smartphone color="var(--primary)" />
            <h2 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 700 }}>2. Portal Paciente (Móvil Simulado)</h2>
          </div>

          {/* Smartphone mockup */}
          <div style={{ 
            margin: '0 auto',
            maxWidth: '340px',
            borderRadius: '36px',
            border: '8px solid #374151',
            backgroundColor: '#111827',
            padding: '18px',
            boxShadow: 'inset 0 0 10px rgba(0,0,0,0.8), 0 10px 25px rgba(0,0,0,0.5)',
            position: 'relative'
          }}>
            <div style={{ 
              width: '100px', 
              height: '18px', 
              backgroundColor: '#374151', 
              borderRadius: '0 0 10px 10px', 
              margin: '-18px auto 15px auto',
              position: 'relative'
            }}></div>

            {/* Mobile App Container */}
            <div style={{ minHeight: '420px', overflowY: 'auto' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '8px', borderBottom: '1px solid rgba(255,255,255,0.05)', marginBottom: '15px' }}>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>12:45 PM</span>
                <span style={{ fontSize: '0.8rem', color: 'var(--primary)', fontWeight: 700 }}>MediSalud App</span>
              </div>

              {/* View switches depending on interaction */}
              {/* Tab navigation inside mockup */}
              <div style={{ display: 'flex', gap: '3px', marginBottom: '15px', padding: '2px', backgroundColor: 'rgba(255,255,255,0.03)', borderRadius: '6px' }}>
                <button style={{ flex: 1, padding: '5px', fontSize: '0.7rem', backgroundColor: bookingStep !== 5 ? '#1f2937' : 'transparent', border: 0, color: 'white', cursor: 'pointer', borderRadius: '4px' }} onClick={() => setBookingStep(1)}>Citas</button>
                <button style={{ flex: 1, padding: '5px', fontSize: '0.7rem', backgroundColor: pagoStatus ? '#1f2937' : 'transparent', border: 0, color: 'white', cursor: 'pointer', borderRadius: '4px' }} onClick={() => setPagoStatus({ mock: true })}>Copago</button>
                <button style={{ flex: 1, padding: '5px', fontSize: '0.7rem', backgroundColor: telemedicinaActive ? '#1f2937' : 'transparent', border: 0, color: 'white', cursor: 'pointer', borderRadius: '4px' }} onClick={() => setTelemedicinaActive(true)}>Telemed</button>
              </div>

              {/* SUB-VIEW 1: BOOKING FLOW */}
              {!pagoStatus && !telemedicinaActive && (
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                    <h4 style={{ margin: 0, fontSize: '0.85rem' }}>Agendar Consulta Médica</h4>
                    <label style={{ fontSize: '0.65rem', display: 'flex', alignItems: 'center', gap: '3px', color: 'var(--text-secondary)', cursor: 'pointer' }}>
                      <input type="checkbox" checked={simulateBookingError} onChange={(e) => setSimulateBookingError(e.target.checked)} />
                      Fallo (RNF-02)
                    </label>
                  </div>

                  {bookingStep === 1 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <p style={{ fontSize: '0.75rem', margin: 0 }}>**Paso 1:** Elija la Especialidad Médica</p>
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleBookingNext}>
                        Cardiología
                      </button>
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} disabled>
                        Pediatría (Sin cupos)
                      </button>
                    </div>
                  )}

                  {bookingStep === 2 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <p style={{ fontSize: '0.75rem', margin: 0 }}>**Paso 2:** Seleccione el Médico Especialista</p>
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleBookingNext}>
                        Dr. Alejandro Tobar
                      </button>
                    </div>
                  )}

                  {bookingStep === 3 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <p style={{ fontSize: '0.75rem', margin: 0 }}>**Paso 3:** Elija la Fecha y Hora</p>
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleBookingNext}>
                        Lunes 20 de Julio - 09:00 AM
                      </button>
                    </div>
                  )}

                  {bookingStep === 4 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <p style={{ fontSize: '0.75rem', margin: 0 }}>**Paso 4:** Confirmar Términos y Condiciones</p>
                      <div style={{ fontSize: '0.65rem', padding: '6px', backgroundColor: 'rgba(255,255,255,0.02)', borderRadius: '4px', border: '1px solid rgba(255,255,255,0.05)' }}>
                        Acepto las políticas de cancelación y copago de la red MediSalud.
                      </div>
                      <button className="btn btn-primary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleConfirmCita}>
                        Aceptar y Reservar
                      </button>
                    </div>
                  )}

                  {bookingStep === 5 && bookingStatus && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.75rem' }}>
                      <div style={{ 
                        padding: '10px', 
                        borderRadius: '6px', 
                        backgroundColor: bookingConflict ? 'rgba(239,68,68,0.1)' : 'rgba(16,185,129,0.1)',
                        border: `1px solid ${bookingConflict ? 'var(--danger)' : 'var(--success)'}`,
                        color: bookingConflict ? 'var(--danger)' : 'var(--success)',
                        fontWeight: 600
                      }}>
                        {bookingStatus.status}
                      </div>
                      <div>Intentos necesarios: {bookingStatus.intentos}</div>
                      
                      {bookingConflict && (
                        <div style={{ fontSize: '0.65rem', color: 'var(--danger)', padding: '5px', border: '1px dashed var(--danger)', borderRadius: '4px' }}>
                          ⚠️ INCIDENTE COMERCIAL: El cupo ya estaba ocupado por otro paciente. Doble reserva registrada en base de datos.
                        </div>
                      )}
                      
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleResetCitasSim}>
                        Nueva Simulación
                      </button>
                    </div>
                  )}

                  {bookingStatus && bookingStatus.error && (
                    <div style={{ 
                      marginTop: '10px',
                      padding: '8px', 
                      borderRadius: '6px', 
                      backgroundColor: 'rgba(239,68,68,0.1)',
                      border: '1px solid var(--danger)',
                      color: 'var(--danger)',
                      fontSize: '0.7rem'
                    }}>
                      {bookingStatus.status} (Intento {bookingIntentos - 1} fallido por expiración)
                    </div>
                  )}
                </div>
              )}

              {/* SUB-VIEW 2: COPAGO FLOW */}
              {pagoStatus && (
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                    <h4 style={{ margin: 0, fontSize: '0.85rem' }}>Pago de Copago de Cita</h4>
                    <label style={{ fontSize: '0.65rem', display: 'flex', alignItems: 'center', gap: '3px', color: 'var(--text-secondary)', cursor: 'pointer' }}>
                      <input type="checkbox" checked={simulatePagoDelay} onChange={(e) => setSimulatePagoDelay(e.target.checked)} />
                      Demora (RNF-03)
                    </label>
                  </div>
                  
                  <div style={{ padding: '10px', backgroundColor: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px', marginBottom: '12px' }}>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Monto a Pagar:</div>
                    <div style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--primary)' }}>$45.00 USD</div>
                    <div style={{ fontSize: '0.65rem', color: 'var(--text-muted)', marginTop: '4px' }}>Tarjeta: VISA **** 1111</div>
                  </div>

                  {(!pagoStatus.status || pagoStatus.reintento_requerido) ? (
                    <button 
                      className={reintentoPago ? "btn btn-danger" : "btn btn-primary"} 
                      style={{ width: '100%', padding: '8px', fontSize: '0.75rem', justifyContent: 'center' }} 
                      onClick={handleProcesarPago}
                    >
                      {reintentoPago ? "⚠️ Reintentar Pago Bloqueado" : "Pagar Copago"}
                    </button>
                  ) : pagoStatus.loading ? (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', alignItems: 'center', fontSize: '0.75rem' }}>
                      <RefreshCw className="animate-spin" size={16} color="var(--primary)" />
                      <span>{pagoStatus.status}</span>
                    </div>
                  ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.75rem' }}>
                      <div style={{ 
                        padding: '10px', 
                        borderRadius: '6px', 
                        backgroundColor: pagoStatus.doble_cobro ? 'rgba(239,68,68,0.1)' : 'rgba(16,185,129,0.1)',
                        border: `1px solid ${pagoStatus.doble_cobro ? 'var(--danger)' : 'var(--success)'}`,
                        color: pagoStatus.doble_cobro ? 'var(--danger)' : 'var(--success)',
                        fontWeight: 600
                      }}>
                        {pagoStatus.status}
                      </div>
                      {pagoStatus.doble_cobro && (
                        <div style={{ fontSize: '0.65rem', color: 'var(--danger)', border: '1px dashed var(--danger)', padding: '5px', borderRadius: '4px' }}>
                          ⚠️ DOBLE COBRO DETECTADO: El reintento procesó un cobro idéntico en la pasarela. Violación del RNF-03.
                        </div>
                      )}
                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={() => { setPagoStatus(null); setReintentoPago(false); }}>
                        Volver a Citas
                      </button>
                    </div>
                  )}

                  {reintentoPago && (
                    <div style={{ 
                      marginTop: '10px',
                      padding: '8px', 
                      borderRadius: '6px', 
                      backgroundColor: 'rgba(245,158,11,0.1)',
                      border: '1px solid var(--warning)',
                      color: 'var(--warning)',
                      fontSize: '0.7rem'
                    }}>
                      ⚠️ El primer intento se ha congelado (demora &gt; 15s). La interfaz se ha bloqueado forzando al usuario a reintentar.
                    </div>
                  )}
                </div>
              )}

              {/* SUB-VIEW 3: TELEMEDICINA FLOW */}
              {telemedicinaActive && (
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                    <h4 style={{ margin: 0, fontSize: '0.85rem' }}>Videoconsulta Remota</h4>
                    <label style={{ fontSize: '0.65rem', display: 'flex', alignItems: 'center', gap: '3px', color: 'var(--text-secondary)', cursor: 'pointer' }}>
                      <input type="checkbox" checked={simulateTelemedicinaError} onChange={(e) => setSimulateTelemedicinaError(e.target.checked)} />
                      Fallo (RNF-05)
                    </label>
                  </div>

                  {!telemedicinaStatus ? (
                    <button className="btn btn-primary" style={{ width: '100%', padding: '8px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={handleStartTelemedicina}>
                      Ingresar a Sala Virtual
                    </button>
                  ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <div style={{ 
                        height: '140px', 
                        backgroundColor: '#1f2937', 
                        borderRadius: '8px', 
                        display: 'flex', 
                        flexDirection: 'column',
                        alignItems: 'center', 
                        justifyContent: 'center',
                        position: 'relative',
                        border: `2px solid ${telemedicinaStreamError ? 'var(--danger)' : 'var(--success)'}`
                      }}>
                        {telemedicinaStreamError ? (
                          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '5px' }}>
                            <AlertOctagon color="var(--danger)" size={28} />
                            <span style={{ fontSize: '0.7rem', color: 'var(--danger)', fontWeight: 700 }}>LLAMADA CAÍDA (RNF-05)</span>
                          </div>
                        ) : (
                          <>
                            <PhoneCall color="var(--success)" className="animate-pulse" size={24} />
                            <span style={{ fontSize: '0.75rem', color: 'white', marginTop: '10px' }}>Dra. Elena Rossi (Cardióloga)</span>
                            <span style={{ fontSize: '0.65rem', color: 'var(--text-secondary)' }}>00:18 min</span>
                          </>
                        )}
                      </div>

                      <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textAlign: 'center' }}>
                        {telemedicinaStatus}
                      </div>

                      <button className="btn btn-secondary" style={{ padding: '6px', fontSize: '0.75rem', justifyContent: 'center' }} onClick={() => { setTelemedicinaActive(false); setTelemedicinaStatus(null); setTelemedicinaStreamError(false); }}>
                        Salir de Telemedicina
                      </button>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>

          {/* Context Coverage Simulator buttons */}
          <div style={{ marginTop: '20px', padding: '15px', border: '1px solid var(--border-color)', borderRadius: '10px', backgroundColor: 'rgba(255,255,255,0.01)' }}>
            <span style={{ fontWeight: 600, fontSize: '0.85rem', display: 'block', marginBottom: '10px' }}>Simular Limitaciones de Contexto (ISO 25022)</span>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '10px' }}>
              <button className="btn btn-secondary" style={{ fontSize: '0.75rem', padding: '8px', justifyContent: 'center' }} onClick={handleMobileContextError}>
                <Smartphone size={14} /> Botón Móvil Falla
              </button>
              <button className="btn btn-secondary" style={{ fontSize: '0.75rem', padding: '8px', justifyContent: 'center' }} onClick={handleTabletContextError}>
                <Tablet size={14} /> Foto Tablet Falla
              </button>
            </div>
            <button className="btn btn-secondary" style={{ width: '100%', fontSize: '0.75rem', padding: '8px', justifyContent: 'center' }} onClick={handleLabIntegrationError}>
              <AlertTriangle size={14} color="var(--warning)" /> Fallo RabbitMQ Lab
            </button>
          </div>
        </section>

        {/* Column 3: Live Audit Panel */}
        <section className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '20px', borderBottom: '1px solid var(--border-color)', paddingBottom: '10px' }}>
            <Database color="var(--primary)" />
            <h2 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 700 }}>3. Panel de Auditoría e ISO 25022</h2>
          </div>

          {/* Statistics summary */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '20px' }}>
            <div style={{ padding: '10px', backgroundColor: 'rgba(14,165,233,0.05)', border: '1px solid rgba(14,165,233,0.15)', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--primary)' }}>{auditStats.total_incidentes}</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Incidentes Registrados</div>
            </div>
            <div style={{ padding: '10px', backgroundColor: 'rgba(239,68,68,0.05)', border: '1px solid rgba(239,68,68,0.15)', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--danger)' }}>{auditStats.violaciones_rnf}</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Violaciones de RNF</div>
            </div>
          </div>

          {/* Counts by category */}
          <div style={{ marginBottom: '20px', padding: '12px', border: '1px solid var(--border-color)', borderRadius: '10px', backgroundColor: 'rgba(255,255,255,0.01)' }}>
            <span style={{ fontSize: '0.8rem', fontWeight: 700, display: 'block', marginBottom: '8px' }}>Distribución ISO/IEC 25022</span>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '0.75rem' }}>
              {['Efectividad', 'Eficiencia', 'Satisfacción', 'Libertad de Riesgo', 'Cobertura de Contexto'].map(cat => {
                const count = auditStats.caracteristicas[cat] || 0;
                const pct = auditStats.total_incidentes > 0 ? (count / auditStats.total_incidentes) * 100 : 0;
                
                // Color mapping
                const colors = {
                  'Efectividad': 'var(--primary)',
                  'Eficiencia': 'var(--warning)',
                  'Satisfacción': '#c084fc',
                  'Libertad de Riesgo': 'var(--danger)',
                  'Cobertura de Contexto': 'var(--success)'
                };

                return (
                  <div key={cat} style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ flex: 2, textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{cat}</span>
                    <div style={{ flex: 3, height: '8px', backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: '4px', overflow: 'hidden' }}>
                      <div style={{ width: `${pct}%`, height: '100%', backgroundColor: colors[cat] || 'white' }}></div>
                    </div>
                    <span style={{ flex: 1, textAlign: 'right', fontWeight: 600 }}>{count} ({Math.round(pct)}%)</span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Audit events feed */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
            <span style={{ fontSize: '0.85rem', fontWeight: 700 }}>Trazabilidad de Logs en Vivo</span>
            <button 
              onClick={async () => {
                // We don't have a direct clear endpoint, but we can restart by just reloading or notifying
                alert("Consola de base de datos PostgreSQL de auditoría activa.");
              }}
              style={{ fontSize: '0.7rem', padding: '4px 8px', backgroundColor: 'transparent', color: 'var(--text-secondary)', border: '1px solid var(--border-color)', borderRadius: '4px', cursor: 'pointer' }}
            >
              Auditar Postgres
            </button>
          </div>

          <div style={{ 
            height: '240px', 
            overflowY: 'auto', 
            border: '1px solid var(--border-color)', 
            borderRadius: '10px', 
            backgroundColor: '#070a12',
            padding: '5px'
          }}>
            {auditLogs.length === 0 ? (
              <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                Ningún incidente registrado en auditoría. Active un fallo y realice una acción.
              </div>
            ) : (
              auditLogs.map(log => {
                const colors = {
                  'Efectividad': 'var(--primary)',
                  'Eficiencia': 'var(--warning)',
                  'Satisfacción': '#c084fc',
                  'Libertad de Riesgo': 'var(--danger)',
                  'Cobertura de Contexto': 'var(--success)'
                };
                
                return (
                  <div 
                    key={log.id} 
                    onClick={() => setSelectedLog(log)}
                    style={{ 
                      padding: '8px 10px', 
                      borderBottom: '1px solid rgba(255,255,255,0.03)', 
                      cursor: 'pointer',
                      fontSize: '0.75rem',
                      transition: 'background-color 0.2s',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center'
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.02)'}
                    onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
                  >
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: '5px' }}>
                        <span style={{ 
                          width: '6px', 
                          height: '6px', 
                          borderRadius: '50%', 
                          backgroundColor: colors[log.caracteristica_iso_25022] || 'white'
                        }}></span>
                        <span style={{ textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{log.descripcion}</span>
                      </div>
                      <div style={{ color: 'var(--text-muted)', fontSize: '0.65rem', marginTop: '2px' }}>
                        {log.fecha} | Sede: {log.sede} | {log.rol_usuario}
                      </div>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '3px' }}>
                      <span style={{ 
                        fontSize: '0.6rem', 
                        padding: '2px 6px', 
                        borderRadius: '10px', 
                        backgroundColor: 'rgba(255,255,255,0.05)', 
                        border: `1px solid ${colors[log.caracteristica_iso_25022] || 'white'}`,
                        color: colors[log.caracteristica_iso_25022] || 'white',
                        fontWeight: 600
                      }}>
                        {log.caracteristica_iso_25022}
                      </span>
                      {log.violacion_rnf && (
                        <span style={{ fontSize: '0.55rem', color: 'var(--danger)', fontWeight: 700 }}>{log.violacion_rnf}</span>
                      )}
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </section>
      </div>

      {/* Log Detail Modal */}
      {selectedLog && (
        <div style={{ 
          position: 'fixed', 
          top: 0, 
          left: 0, 
          right: 0, 
          bottom: 0, 
          backgroundColor: 'rgba(0,0,0,0.8)', 
          backdropFilter: 'blur(5px)', 
          display: 'flex', 
          justifyContent: 'center', 
          alignItems: 'center',
          zIndex: 1000
        }}>
          <div className="glass-panel" style={{ padding: '24px', maxWidth: '550px', width: '90%', border: '1px solid rgba(14,165,233,0.3)' }}>
            <h3 style={{ margin: '0 0 15px 0', fontSize: '1.2rem', color: 'var(--primary)', borderBottom: '1px solid var(--border-color)', paddingBottom: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Cpu size={20} /> Detalle de Auditoría del Incidente
            </h3>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', fontSize: '0.85rem' }}>
              <div>
                <strong style={{ color: 'var(--text-secondary)' }}>Módulo Afectado:</strong> {selectedLog.modulo}
              </div>
              <div>
                <strong style={{ color: 'var(--text-secondary)' }}>Descripción del Log:</strong> {selectedLog.descripcion}
              </div>
              <div style={{ display: 'flex', gap: '20px' }}>
                <div><strong style={{ color: 'var(--text-secondary)' }}>Sede:</strong> {selectedLog.sede}</div>
                <div><strong style={{ color: 'var(--text-secondary)' }}>Rol:</strong> {selectedLog.rol_usuario}</div>
              </div>
              <div>
                <strong style={{ color: 'var(--text-secondary)' }}>Característica ISO/IEC 25022:</strong>{' '}
                <span style={{ color: selectedLog.caracteristica_iso_25022 === 'Libertad de Riesgo' ? 'var(--danger)' : 'var(--primary)', fontWeight: 700 }}>
                  {selectedLog.caracteristica_iso_25022}
                </span>
              </div>
              {selectedLog.violacion_rnf && (
                <div>
                  <strong style={{ color: 'var(--text-secondary)' }}>Requerimiento No Funcional Violado:</strong>{' '}
                  <span style={{ color: 'var(--warning)', fontWeight: 700 }}>{selectedLog.violacion_rnf}</span>
                </div>
              )}
              <div>
                <strong style={{ color: 'var(--text-secondary)' }}>Justificación Técnica:</strong>
                <p style={{ margin: '5px 0 0 0', padding: '10px', backgroundColor: 'rgba(255,255,255,0.02)', border: '1px solid var(--border-color)', borderRadius: '6px', fontSize: '0.8rem', lineHeight: '1.4' }}>
                  {selectedLog.justificacion_tecnica}
                </p>
              </div>
              
              <div style={{ marginTop: '10px', padding: '10px', backgroundColor: '#070a12', border: '1px solid var(--border-color)', borderRadius: '6px', fontSize: '0.75rem', fontFamily: 'monospace' }}>
                <div style={{ color: 'var(--text-muted)', marginBottom: '5px' }}>-- Auditoría SQL Interna (PostgreSQL)</div>
                <span style={{ color: '#10b981' }}>INSERT INTO</span> incidente_logs (fecha, modulo, descripcion, rol_usuario, sede, caracteristica_iso_25022, justificacion_tecnica) <span style={{ color: '#eab308' }}>VALUES</span> ('{selectedLog.fecha}', '{selectedLog.modulo}', '{selectedLog.descripcion}', '{selectedLog.rol_usuario}', '{selectedLog.sede}', '{selectedLog.caracteristica_iso_25022}', ...);
              </div>
            </div>
            
            <button className="btn btn-primary" style={{ width: '100%', marginTop: '20px', justifyContent: 'center' }} onClick={() => setSelectedLog(null)}>
              Cerrar Detalle
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
