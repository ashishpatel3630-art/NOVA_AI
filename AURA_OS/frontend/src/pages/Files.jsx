import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { FolderOpen, Upload, Search } from 'lucide-react'

function FilesPage() {
  const [files, setFiles] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://localhost:8000/api/files')
      .then((res) => res.json())
      .then((data) => {
        setFiles(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
        <div>
          <div style={{ color:'#6366f1', fontWeight:700 }}>File Manager</div>
          <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Organize work effortlessly</h1>
        </div>
        <button className="nav-btn" style={{ background:'#1e293b' }}>
          <Upload size={16} /> Upload
        </button>
      </div>

      <div className="card" style={{ display:'flex', gap:'10px', alignItems:'center' }}>
        <Search size={16} color="#94a3b8" />
        <input style={{ flex:1, border:'none', outline:'none', background:'transparent', color:'#fff' }} placeholder="Search files" />
      </div>

      <div className="grid grid-3">
        {loading ? <div style={{ color:'#94a3b8' }}>Loading files…</div> : files.map((file) => (
          <motion.div key={file.path} className="card" whileHover={{ y: -4, scale: 1.01 }}>
            <div style={{ display:'flex', alignItems:'center', gap:'8px', marginBottom:'8px' }}>
              <FolderOpen size={18} color="#6366f1" />
              <strong>{file.name}</strong>
            </div>
            <div style={{ color:'#94a3b8' }}>{file.is_dir ? 'Folder' : 'File'}</div>
            <div style={{ color:'#94a3b8', fontSize:'0.9rem', marginTop:'6px' }}>{file.size} bytes</div>
          </motion.div>
        ))}
      </div>
    </div>
  )
}

export default FilesPage
