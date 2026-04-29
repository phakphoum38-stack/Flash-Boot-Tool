import React from "react";

export default function DeviceSelect({ device, setDevice }) {
  return (
    <input
      placeholder="/dev/sdb"
      value={device}
      onChange={(e) => setDevice(e.target.value)}
      style={{ padding: 10, width: "100%" }}
    />
  );
}
