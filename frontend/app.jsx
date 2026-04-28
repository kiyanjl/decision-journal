const { useState, useEffect, useRef } = React;

function App() {
    const [version, setVersion] = useState("v1.2.0");
    const [decision, setDecision] = useState(null);
    const [events, setEvents] = useState([]);
    const [humanTrace, setHumanTrace] = useState([]);
    const [aiTrace, setAiTrace] = useState([]);
    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);

    const API_BASE = "http://localhost:8000";

    const fetchData = async () => {
        setLoading(true);
        try {
            const [decRes, evRes, histRes, humanRes, aiRes] = await Promise.all([
                fetch(`${API_BASE}/decision/${version}`),
                fetch(`${API_BASE}/timeline/${version}`),
                fetch(`${API_BASE}/history`),
                fetch(`${API_BASE}/trace/human/${version}`),
                fetch(`${API_BASE}/trace/ai/${version}`)
            ]);
            
            if (decRes.ok) setDecision(await decRes.json());
            if (evRes.ok) setEvents(await evRes.json());
            if (histRes.ok) setHistory(await histRes.json());
            if (humanRes.ok) setHumanTrace(await humanRes.json());
            if (aiRes.ok) setAiTrace(await aiRes.json());
        } catch (error) {
            console.error("Failed to fetch data", error);
        }
        setLoading(false);
    };

    useEffect(() => {
        fetchData();
    }, [version]);

    if (loading) return <div className="p-10 text-center font-bold text-xl">Loading Decision Journal...</div>;
    if (!decision) return (
        <div className="p-10 text-center text-red-600">
            <h1 className="text-2xl font-bold mb-4">API Offline or No Data</h1>
            <p>Please start the FastAPI server and seed the database.</p>
        </div>
    );

    const handleTraceClick = async (traceId) => {
        try {
            const res = await fetch(`${API_BASE}/trace/${traceId}`);
            if (!res.ok) {
                alert(`Traceability data for ${traceId} not found.`);
                return;
            }
            const data = await res.json();
            alert(`Trace for ${traceId}:\n\nEvents: ${data.events.join(', ')}\nDecision Version: ${data.decision}\n\nDetails:\n${JSON.stringify(data.events_details, null, 2)}`);
        } catch (error) {
            console.error("Failed to fetch trace data", error);
            alert("Could not fetch traceability data. Is the API running?");
        }
    };

    const isRejected = decision.status === "REJECTED";

    return (
        <div className="max-w-6xl mx-auto p-6">
            <header className="flex justify-between items-center mb-8 border-b pb-4">
                <div>
                    <h1 className="text-3xl font-extrabold text-gray-900">Decision Journal</h1>
                    <p className="text-sm text-gray-500 mt-1">Final Audit & Traceability System</p>
                </div>
                <div className="flex gap-2 items-center">
                    <span className="font-semibold">History:</span>
                    {history.map(h => (
                        <button 
                            key={h.version}
                            onClick={() => setVersion(h.version)}
                            className={`px-3 py-1 rounded text-sm font-bold border ${h.version === version ? 'bg-blue-600 text-white border-blue-600' : 'bg-white text-gray-700 hover:bg-gray-100'}`}
                        >
                            {h.version} {h.status === 'APPROVED' ? '✔' : '✖'}
                        </button>
                    ))}
                </div>
            </header>

            <div className="grid-layout">
                {/* Main Content */}
                <div>
                    {/* Summary Header */}
                    <div className={`card text-white flex justify-between items-center ${isRejected ? 'bg-red-600' : 'bg-green-600'}`}>
                        <div>
                            <h2 className="text-2xl font-bold">Version {decision.version}</h2>
                            <p className="opacity-80">Timestamp: {new Date(decision.timestamp).toLocaleString()}</p>
                        </div>
                        <div className="text-right">
                            <div className="text-xl font-black tracking-wider">{decision.status}</div>
                            <div className="text-sm">Risk: {isRejected ? 'HIGH' : 'LOW'}</div>
                        </div>
                    </div>

                    {/* Problems */}
                    {decision.problems.length > 0 && (
                        <div className="card border-l-4 border-red-500">
                            <h3 className="text-lg font-bold text-red-600 mb-2">🔴 Key Problems</h3>
                            <ul className="list-disc pl-5 space-y-1">
                                {decision.problems.map((p, i) => <li key={i} className="text-gray-800">{p}</li>)}
                            </ul>
                        </div>
                    )}

                    {/* Decision Journal Details */}
                    <div className="card">
                        <h3 className="text-lg font-bold text-gray-800 mb-3">📄 Decision Reasoning</h3>
                        <div className="space-y-3 bg-gray-50 p-4 rounded border">
                            <div><span className="font-bold text-gray-600">Change context:</span> {decision.decision.change}</div>
                            <div><span className="font-bold text-gray-600">System Impact:</span> {decision.decision.impact}</div>
                            <div><span className="font-bold text-gray-600">Assumption:</span> {decision.decision.assumption}</div>
                            <div><span className="font-bold text-gray-600">Alternatives:</span> {decision.decision.alternatives}</div>
                            <div>
                                <span className="font-bold text-gray-600">AI Recommendation:</span> 
                                <span className={`ml-2 px-2 py-1 text-xs font-bold rounded ${decision.decision.recommendation === 'Delay' ? 'bg-yellow-200 text-yellow-800' : 'bg-green-200 text-green-800'}`}>
                                    {decision.decision.recommendation}
                                </span>
                            </div>
                        </div>
                    </div>

                    {/* Timeline */}
                    <div className="card">
                        <h3 className="text-lg font-bold text-gray-800 mb-4">🕒 Event Timeline</h3>
                        <div className="relative border-l-2 border-gray-200 ml-3 space-y-6">
                            {events.map((ev, i) => (
                                <div key={i} className="pl-6 relative">
                                    <div className={`absolute w-3 h-3 rounded-full -left-[7px] top-1.5 ${ev.type.includes('FAIL') || ev.type.includes('CONFLICT') || ev.type.includes('REJECT') ? 'bg-red-500' : 'bg-blue-500'}`}></div>
                                    <div className="text-xs text-gray-500 font-mono">{new Date(ev.timestamp).toLocaleTimeString()}</div>
                                    <div className="font-bold text-gray-800">{ev.type} <span className="text-sm font-normal text-gray-500 bg-gray-100 px-1 rounded ml-1">{ev.layer}</span></div>
                                    <div className="text-sm text-gray-600">{ev.description}</div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

                {/* Sidebar */}
                <div>
                    {/* Graph */}
                    <div className="card">
                        <h3 className="text-lg font-bold text-gray-800 mb-4">📊 Test Coverage</h3>
                        <CoverageChart summary={decision.summary} />
                    </div>

                    {/* Traceability (Example) */}
                    <div className="card bg-blue-50">
                        <h3 className="text-lg font-bold text-blue-800 mb-3">🔗 Traceability Links</h3>
                        <p className="text-sm text-gray-600 mb-4">Click to view requirement trace</p>

                        <div className="space-y-2">
                            <button onClick={() => handleTraceClick('REQ-05')} className="w-full text-left p-2 bg-white border border-blue-200 rounded hover:bg-blue-100 text-sm font-medium text-blue-700">
                                Trace REQ-05 (Missing Coverage)
                            </button>
                            <button onClick={() => handleTraceClick('REQ-10')} className="w-full text-left p-2 bg-white border border-blue-200 rounded hover:bg-blue-100 text-sm font-medium text-blue-700">
                                Trace REQ-10 (Test T-02 Failure)
                            </button>
                        </div>
                    </div>

                    {/* Human Traceability */}
                    {humanTrace.length > 0 && (
                        <div className="card bg-purple-50">
                            <h3 className="text-lg font-bold text-purple-800 mb-3">👤 Human Traceability</h3>
                            <ul className="space-y-2 text-sm text-gray-700">
                                {humanTrace.map((ht, i) => (
                                    <li key={i}><strong>{ht.role}:</strong> {ht.person}</li>
                                ))}
                            </ul>
                        </div>
                    )}

                    {/* AI Traceability */}
                    {aiTrace.length > 0 && (
                        <div className="card bg-indigo-50">
                            <h3 className="text-lg font-bold text-indigo-800 mb-3">🤖 AI Traceability</h3>
                            <ul className="space-y-2 text-sm text-gray-700 list-disc pl-5">
                                {aiTrace.map((at, i) => (
                                    <li key={i}><strong>{at.step}:</strong> {at.details}</li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

// Simple wrapper for Chart.js
function CoverageChart({ summary }) {
    const chartRef = useRef(null);
    const chartInstance = useRef(null);

    useEffect(() => {
        if (chartInstance.current) {
            chartInstance.current.destroy();
        }

        const ctx = chartRef.current.getContext('2d');
        chartInstance.current = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Passed', 'Failed', 'Missing'],
                datasets: [{
                    label: 'Tests',
                    data: [
                        summary.tested, 
                        (summary.total_req - summary.tested - summary.missing), 
                        summary.missing
                    ],
                    backgroundColor: ['#22c55e', '#ef4444', '#f59e0b'],
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });

        return () => {
            if (chartInstance.current) {
                chartInstance.current.destroy();
            }
        }
    }, [summary]);

    return <canvas ref={chartRef}></canvas>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);