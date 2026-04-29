export async function streamJSONLines(res, onData) {
  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split("\n");

    for (let line of lines) {
      if (!line.trim()) continue;
      try {
        onData(JSON.parse(line));
      } catch (e) {
        console.warn("parse fail:", line);
      }
    }
  }
}
