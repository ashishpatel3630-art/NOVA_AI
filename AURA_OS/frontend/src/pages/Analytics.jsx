import { ResponsiveContainer, AreaChart, Area, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts'

const data = [
  { month: 'Jan', score: 62 },
  { month: 'Feb', score: 70 },
  { month: 'Mar', score: 74 },
  { month: 'Apr', score: 82 },
  { month: 'May', score: 88 },
  { month: 'Jun', score: 91 },
]

function AnalyticsPage() {
  return (
    <div style={{ display:'grid', gap:'16px' }}>
      <div>
        <div style={{ color:'#6366f1', fontWeight:700 }}>Analytics</div>
        <h1 style={{ margin:'4px 0', fontSize:'1.7rem' }}>Performance insights</h1>
      </div>

      <div className="card">
        <h3 style={{ marginTop:0 }}>Productivity trend</h3>
        <div style={{ width:'100%', height:260 }}>
          <ResponsiveContainer>
            <AreaChart data={data}>
              <CartesianGrid stroke="#334155" strokeDasharray="3 3" />
              <XAxis dataKey="month" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip />
              <Area type="monotone" dataKey="score" stroke="#6366f1" fill="#6366f1" fillOpacity={0.25} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}

export default AnalyticsPage
