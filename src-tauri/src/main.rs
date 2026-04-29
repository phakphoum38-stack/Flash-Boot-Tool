#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod commands;

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::flash_dd,
            commands::smart_flash,
            commands::ventoy
        ])
        .run(tauri::generate_context!())
        .expect("error running app");
}
