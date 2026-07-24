import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { PlusCircle, X } from 'lucide-react'

function TasksPage() {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [submitting, setSubmitting] = useState(false)
  const [form, setForm] = useState({ title: '', description: '', priority: 'Medium', deadline: '' })

  const loadTasks = () => {
    setLoading(true)
    fetch('http://localhost:8000/api/tasks')
      .then((res) => res.json())
      .then((data) => {
        setTasks(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }

  useEffect(() => {
    loadTasks()
  }, [])

  const handleSubmit = async (event) => {
    event.preventDefault()
    if (!form.title.trim()) return

    setSubmitting(true)
    const response = await fetch('http://localhost:8000/api/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: form.title.trim(),
        description: form.description.trim(),
        priority: form.priority,
        deadline: form.deadline,
      }),
    })

    if (response.ok) {
      const created = await response.json()
      setTasks((prev) => [{ id: created.id, ...form, title: form.title.trim(), description: form.description.trim(), status: 'Pending' }, ...prev])
      setShowForm(false)
      setForm({ title: '', description: '', priority: 'Medium', deadline: '' })
    }
    setSubmitting(false)
  }

  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
        <div>
          <div style={{ color:'#6366f1', fontWeight:700 }}>Task Management</div>
          <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Plan work with clarity</h1>
        </div>
        <button className="nav-btn" style={{ background:'#1e293b' }} onClick={() => setShowForm((prev) => !prev)}>
          <PlusCircle size={16} /> {showForm ? 'Close' : 'New Task'}
        </button>
      </div>

      {showForm && (
        <form className="card" onSubmit={handleSubmit} style={{ display:'grid', gap:'12px' }}>
          <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
            <h3 style={{ margin: 0 }}>Add a task</h3>
            <button type="button" className="nav-btn" onClick={() => setShowForm(false)} style={{ padding: 6, background: 'transparent' }}>
              <X size={16} />
            </button>
          </div>
          <input value={form.title} onChange={(event) => setForm((prev) => ({ ...prev, title: event.target.value }))} placeholder="Task title" style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} required />
          <textarea value={form.description} onChange={(event) => setForm((prev) => ({ ...prev, description: event.target.value }))} placeholder="Short description" rows="3" style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} />
          <div style={{ display:'grid', gap:'10px', gridTemplateColumns:'repeat(2, minmax(0, 1fr))' }}>
            <select value={form.priority} onChange={(event) => setForm((prev) => ({ ...prev, priority: event.target.value }))} style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }}>
              <option value="High">High</option>
              <option value="Medium">Medium</option>
              <option value="Low">Low</option>
            </select>
            <input type="date" value={form.deadline} onChange={(event) => setForm((prev) => ({ ...prev, deadline: event.target.value }))} style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} />
          </div>
          <button type="submit" className="nav-btn" disabled={submitting} style={{ justifyContent:'center', background:'#6366f1' }}>
            {submitting ? 'Saving…' : 'Save task'}
          </button>
        </form>
      )}

      <div className="card">
        <table style={{ width:'100%', borderCollapse:'collapse' }}>
          <thead>
            <tr style={{ color:'#94a3b8', textAlign:'left' }}>
              <th style={{ padding:'10px 0' }}>Title</th>
              <th style={{ padding:'10px 0' }}>Priority</th>
              <th style={{ padding:'10px 0' }}>Status</th>
              <th style={{ padding:'10px 0' }}>Deadline</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan="4" style={{ padding:'16px 0', color:'#94a3b8' }}>Loading tasks…</td></tr>
            ) : tasks.map((task) => (
              <motion.tr key={task.id} whileHover={{ background:'rgba(255,255,255,0.04)' }} style={{ borderTop:'1px solid rgba(255,255,255,0.08)' }}>
                <td style={{ padding:'12px 0' }}>
                  <div style={{ fontWeight:700 }}>{task.title}</div>
                  <div style={{ color:'#94a3b8', fontSize:'0.9rem' }}>{task.description}</div>
                </td>
                <td>{task.priority}</td>
                <td>{task.status}</td>
                <td>{task.deadline}</td>
              </motion.tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default TasksPage
