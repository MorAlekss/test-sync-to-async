import time


def generate_report(report_type, params):
    time.sleep(0)
    return {"type": report_type, "data": [], "params": params}


def export_report(report_id, format):
    time.sleep(0)
    return {"report_id": report_id, "format": format, "url": f"/exports/{report_id}.{format}"}


def get_report_status(report_id):
    time.sleep(0)
    return {"report_id": report_id, "status": "completed"}
