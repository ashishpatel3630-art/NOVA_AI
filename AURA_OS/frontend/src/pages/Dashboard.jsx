import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ArrowUpRight, CheckCircle2, Clock3, FileText, Sparkles } from 'lucide-react'
import { ResponsiveContainer, LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts'

const chartData = [
  { day: 'Mon', productivity: 72 },
  { day: 'Tue', productivity: 84 },
  { day: 'Wed', productivity: 69 },
  { day: 'Thu', productivity: 91 },
  { day: 'Fri', productivity: 88 },
  { day: 'Sat', productivity: 76 },
  { day: 'Sun', productivity: 80 },
]

function DashboardPage() {
  const navigate = useNavigate()
  const [stats, setStats] = useState({ tasks: 0, completed: 0, pending: 0, notes: 0, recent_tasks: [] })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://localhost:8000/api/dashboard')
      .then((res) => res.json())
      .then((data) => {
        setStats(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
        <div>
          <div style={{ color:'#6366f1', fontWeight:700 }}>Executive Overview</div>
          <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Your digital command center</h1>
        </div>
        <div className="card" style={{ display:'flex', alignItems:'center', gap:'8px' }}>
          <Sparkles size={16} color="#22c55e" />
          Focus score 92%
        </div>
      </div>

      <div className="grid grid-4">
        {[
          ['Total Tasks', stats.tasks, <CheckCircle2 size={18} color="#6366f1" />],
          ['Completed', stats.completed, <CheckCircle2 size={18} color="#22c55e" />],
          ['Pending', stats.pending, <Clock3 size={18} color="#f59e0b" />],
          ['Notes', stats.notes, <FileText size={18} color="#38bdf8" />],
        ].map(([label, value, icon]) => (
          <motion.div key={label} className="card" whileHover={{ y: -4, scale: 1.01 }}>
            <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
              <div style={{ color:'#94a3b8' }}>{label}</div>
              {icon}
            </div>
            <div style={{ fontSize:'1.8rem', fontWeight:800, marginTop:'8px' }}>{loading ? '—' : value}</div>
          </motion.div>
        ))}
      </div>

      <div className="grid grid-2">
        <div className="card">
          <div style={{ display:'flex', justifyContent:'space-between', marginBottom:'12px' }}>
            <h3 style={{ margin:0 }}>Weekly Productivity</h3>
            <div style={{ color:'#22c55e', fontWeight:700 }}>+12%</div>
          </div>
          <div style={{ width:'100%', height:220 }}>
            <ResponsiveContainer>
              <LineChart data={chartData}>
                <CartesianGrid stroke="#334155" strokeDasharray="3 3" />
                <XAxis dataKey="day" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip />
                <Line type="monotone" dataKey="productivity" stroke="#6366f1" strokeWidth={3} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card">
          <div style={{ display:'flex', justifyContent:'space-between', marginBottom:'12px' }}>
            <h3 style={{ margin:0 }}>Task Completion</h3>
            <div style={{ color:'#22c55e', fontWeight:700 }}>Stable</div>
          </div>
          <div style={{ width:'100%', height:220 }}>
            <ResponsiveContainer>
              <BarChart data={chartData}>
                <CartesianGrid stroke="#334155" strokeDasharray="3 3" />
                <XAxis dataKey="day" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip />
                <Bar dataKey="productivity" fill="#22c55e" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid grid-2">
        <div className="card">
          <h3 style={{ marginTop:0 }}>Upcoming Deadlines</h3>
          {loading ? <div style={{ color:'#94a3b8' }}>Loading tasks…</div> : stats.recent_tasks.map((task) => (
            <div key={task.title} style={{ display:'flex', justifyContent:'space-between', padding:'10px 0', borderBottom:'1px solid rgba(255,255,255,0.08)' }}>
              <div>
                <div style={{ fontWeight:700 }}>{task.title}</div>
                <div style={{ color:'#94a3b8', fontSize:'0.9rem' }}>{task.priority}</div>
              </div>
              <div style={{ color:'#6366f1', fontWeight:600 }}>{task.deadline}</div>
            </div>
          ))}
        </div>

        <div className="card">
          <h3 style={{ marginTop:0 }}>Quick Actions</h3>
          <div style={{ display:'grid', gap:'10px' }}>
            <button className="nav-btn" style={{ justifyContent:'space-between', background:'#1e293b' }} onClick={() => navigate('/tasks', { state: { openForm: true } })}>
              <span>New task</span><ArrowUpRight size={16} />
            </button>
            <button className="nav-btn" style={{ justifyContent:'space-between', background:'#1e293b' }} onClick={() => navigate('/notes', { state: { openForm: true } })}>
              <span>Capture note</span><ArrowUpRight size={16} />
            </button>
            <button className="nav-btn" style={{ justifyContent:'space-between', background:'#1e293b' }}>
              <span>Review analytics</span><ArrowUpRight size={16} />
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DashboardPage
