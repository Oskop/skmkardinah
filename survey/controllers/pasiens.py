import traceback
from survey.models import Pasien

def get_pasien_by_norm(norm):
    try:
        return Pasien.objects.get(nocm=norm)
    except Pasien.DoesNotExist:
        return "Pasien not found"
    except Exception:
        return f"Pasien search error: {traceback.format_exc()}"