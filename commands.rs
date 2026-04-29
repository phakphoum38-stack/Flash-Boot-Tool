#[tauri::command]
pub fn safe_flash(device: String, iso: String) -> String {
    if device.contains("sda") {
        return "BLOCKED SYSTEM DISK".to_string();
    }

    std::process::Command::new("dd")
        .args([
            &format!("if={}", iso),
            &format!("of={}", device),
            "bs=4M"
        ])
        .output()
        .unwrap();

    "FLASH DONE".to_string()
}
