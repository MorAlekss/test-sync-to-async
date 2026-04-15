import asyncio


async def generate_report(report_type, params):
    await asyncio.sleep(0)
    return {"type": report_type, "data": [], "params": params}


async def export_report(report_id, format):
    await asyncio.sleep(0)
    return {"report_id": report_id, "format": format, "url": f"/exports/{report_id}.{format}"}


async def get_report_status(report_id):
    await asyncio.sleep(0)
    return {"report_id": report_id, "status": "completed"}
