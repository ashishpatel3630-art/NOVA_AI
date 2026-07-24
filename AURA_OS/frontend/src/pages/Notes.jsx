import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { PlusCircle, X } from 'lucide-react'

function NotesPage() {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [submitting, setSubmitting] = useState(false)
  const [form, setForm] = useState({ title: '', category: 'General', content: '' })

  const loadNotes = () => {
    setLoading(true)
    fetch('http://localhost:8000/api/notes')
      .then((res) => res.json())
      .then((data) => {
        setNotes(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }

  useEffect(() => {
    loadNotes()
  }, [])

  const handleSubmit = async (event) => {
    event.preventDefault()
    if (!form.title.trim()) return

    setSubmitting(true)
    const response = await fetch('http://localhost:8000/api/notes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: form.title.trim(),
        category: form.category,
        content: form.content.trim(),
      }),
    })

    if (response.ok) {
      const created = await response.json()
      setNotes((prev) => [{ id: created.id, ...form, title: form.title.trim(), content: form.content.trim() }, ...prev])
      setShowForm(false)
      setForm({ title: '', category: 'General', content: '' })
    }
    setSubmitting(false)
  }

  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
        <div>
          <div style={{ color:'#6366f1', fontWeight:700 }}>Notes</div>
          <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Capture ideas instantly</h1>
        </div>
        <button className="nav-btn" style={{ background:'#1e293b' }} onClick={() => setShowForm((prev) => !prev)}>
          <PlusCircle size={16} /> {showForm ? 'Close' : 'New Note'}
        </button>
      </div>

      {showForm && (
        <form className="card" onSubmit={handleSubmit} style={{ display:'grid', gap:'12px' }}>
          <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
            <h3 style={{ margin: 0 }}>Add a note</h3>
            <button type="button" className="nav-btn" onClick={() => setShowForm(false)} style={{ padding: 6, background: 'transparent' }}>
              <X size={16} />
            </button>
          </div>
          <input value={form.title} onChange={(event) => setForm((prev) => ({ ...prev, title: event.target.value }))} placeholder="Note title" style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} required />
          <input value={form.category} onChange={(event) => setForm((prev) => ({ ...prev, category: event.target.value }))} placeholder="Category" style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} />
          <textarea value={form.content} onChange={(event) => setForm((prev) => ({ ...prev, content: event.target.value }))} placeholder="Write your note here" rows="4" style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.12)', background:'#0f172a', color:'#fff' }} />
          <button type="submit" className="nav-btn" disabled={submitting} style={{ justifyContent:'center', background:'#22c55e' }}>
            {submitting ? 'Saving…' : 'Save note'}
          </button>
        </form>
      )}

      <div className="grid grid-3">
        {loading ? <div style={{ color:'#94a3b8' }}>Loading notes…</div> : notes.map((note) => (
          <motion.div key={note.id} className="card" whileHover={{ y: -4, scale: 1.01 }}>
            <div style={{ color:'#22c55e', fontWeight:700, marginBottom:'8px' }}>{note.category}</div>
            <h3 style={{ margin:'4px 0' }}>{note.title}</h3>
            <p style={{ color:'#cbd5e1', lineHeight:1.6 }}>{note.content}</p>
          </motion.div>
        ))}
      </div>
    </div>
  )
}

export default NotesPage
