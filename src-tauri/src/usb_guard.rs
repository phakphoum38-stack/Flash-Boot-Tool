pub fn is_safe_device(device: &str) -> bool {
    let dangerous = vec!["/dev/sda", "/dev/nvme0n1"];
    !dangerous.contains(&device)
}
