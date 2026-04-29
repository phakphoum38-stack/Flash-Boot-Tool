import { useState } from "react";

export default function SafeConfirmModal({ device, onConfirm }) {
  const [text, setText] = useState("");

  return (
    <div className="glass">
      <h3>⚠️ Dangerous Operation</h3>
      <p>Type device name to confirm: <b>{device}</b></p>

      <input onChange={(e)=>setText(e.target.value)} />

      <button
        disabled={text !== device}
        onClick={onConfirm}
      >
        Confirm
      </button>
    </div>
  );
}
