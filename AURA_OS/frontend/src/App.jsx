import { Routes, Route, NavLink } from 'react-router-dom'
import { motion } from 'framer-motion'
import { LayoutDashboard, CheckSquare, StickyNote, Folder, BarChart3, Wrench, Settings, Sparkles } from 'lucide-react'
import DashboardPage from './pages/Dashboard'
import TasksPage from './pages/Tasks'
import NotesPage from './pages/Notes'
import FilesPage from './pages/Files'
import AnalyticsPage from './pages/Analytics'
import SettingsPage from './pages/Settings'

const navItems = [
  { to: '/', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/tasks', label: 'Tasks', icon: CheckSquare },
  { to: '/notes', label: 'Notes', icon: StickyNote },
  { to: '/files', label: 'Files', icon: Folder },
  { to: '/analytics', label: 'Analytics', icon: BarChart3 },
  { to: '/settings', label: 'Settings', icon: Settings },
]

function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="logo">
          <div className="logo-badge"><Sparkles size={18} /></div>
          <div>
            <div>AURA OS</div>
            <div style={{fontSize:'0.8rem', color:'#94a3b8'}}>Productivity</div>
          </div>
        </div>

        <div className="card">
          <div style={{fontSize:'0.8rem', color:'#94a3b8'}}>Workspace</div>
          <div style={{fontWeight:700, marginTop:6}}>Daily Command Center</div>
        </div>

        <nav style={{ display:'grid', gap:'8px' }}>
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink key={to} to={to} className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}>
              <Icon size={18} />
              <span>{label}</span>
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="content">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.25 }}>
          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/tasks" element={<TasksPage />} />
            <Route path="/notes" element={<NotesPage />} />
            <Route path="/files" element={<FilesPage />} />
            <Route path="/analytics" element={<AnalyticsPage />} />
            <Route path="/settings" element={<SettingsPage />} />
          </Routes>
        </motion.div>
      </main>
    </div>
  )
}

export default App
