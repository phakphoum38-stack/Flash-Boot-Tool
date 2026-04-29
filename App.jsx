import GlassCard from "./components/GlassCard";

export default function App() {
  return (
    <div style={{ padding: 40 }}>
      <h1>⚡ FlashForge Pro</h1>

      <GlassCard>
        <h2>USB Device</h2>
        <button>Detect USB</button>
      </GlassCard>

      <GlassCard>
        <h2>ISO File</h2>
        <button>Select ISO</button>
      </GlassCard>

      <GlassCard>
        <h2>AI Mode</h2>
        <button>Auto Partition + Boot Fix</button>
      </GlassCard>

      <GlassCard>
        <button>🔥 START FLASH</button>
      </GlassCard>
    </div>
  );
}
