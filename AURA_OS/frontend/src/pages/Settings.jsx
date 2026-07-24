import { motion } from 'framer-motion'

function SettingsPage() {
  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div>
        <div style={{ color:'#6366f1', fontWeight:700 }}>Settings</div>
        <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Tune your workspace</h1>
      </div>

      <motion.div className="card" whileHover={{ y: -4 }}>
        <h3 style={{ marginTop:0 }}>Profile</h3>
        <div style={{ display:'grid', gap:'10px' }}>
          <input style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.1)', background:'#0f172a', color:'#fff' }} placeholder="Username" />
          <input style={{ padding:'10px 12px', borderRadius:'10px', border:'1px solid rgba(255,255,255,0.1)', background:'#0f172a', color:'#fff' }} placeholder="Email" />
        </div>
      </motion.div>

      <motion.div className="card" whileHover={{ y: -4 }}>
        <h3 style={{ marginTop:0 }}>Appearance</h3>
        <div style={{ display:'flex', gap:'10px' }}>
          <button className="nav-btn" style={{ background:'#1e293b' }}>Dark</button>
          <button className="nav-btn" style={{ background:'#1e293b' }}>Light</button>
        </div>
      </motion.div>
    </div>
  )
}

export default SettingsPage
