@router.post("/flash")
def flash(data: FlashRequest):

    try:
        verify_device_safe(data.device)
        verify_iso_safe(data.iso)
        reset_abort()

        def gen():
            for update in flash_with_progress(data.iso, data.device):
                yield json.dumps(update) + "\n"

                if update.get("status") == "aborted":
                    return

            result = smart_verify(data.iso, data.device)
            yield json.dumps({"verify": result}) + "\n"

        return StreamingResponse(gen(), media_type="application/x-ndjson")

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
