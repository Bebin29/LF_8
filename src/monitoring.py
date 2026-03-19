"""Modul zur Erfassung von Systemressourcen.

Nutzt psutil zur plattformunabhängigen Erfassung von
Disk, RAM, Prozessen und eingeloggten Nutzern.
"""

from typing import Dict, List

import psutil


class SystemMonitor:
    """Klasse zur plattformunabhängigen Erfassung von Systemressourcen."""

    @staticmethod
    def get_disk_usage(path: str = "/") -> Dict[str, float]:
        """Ermittelt die Festplattenauslastung.

        Args:
            path: Pfad des zu prüfenden Dateisystems.

        Returns:
            Dict mit total, used, free (in GB) und percent.
        """
        try:
            usage = psutil.disk_usage(path)
            return {
                "total_gb": round(usage.total / (1024 ** 3), 2),
                "used_gb": round(usage.used / (1024 ** 3), 2),
                "free_gb": round(usage.free / (1024 ** 3), 2),
                "percent": usage.percent,
            }
        except OSError as e:
            print(f"Fehler beim Lesen der Disk-Daten: {e}")
            return {
                "total_gb": 0.0,
                "used_gb": 0.0,
                "free_gb": 0.0,
                "percent": 0.0,
            }

    @staticmethod
    def get_ram_usage() -> Dict[str, float]:
        """Ermittelt die Arbeitsspeicher-Auslastung.

        Returns:
            Dict mit total, used, available (in GB) und percent.
        """
        mem = psutil.virtual_memory()
        return {
            "total_gb": round(mem.total / (1024 ** 3), 2),
            "used_gb": round(mem.used / (1024 ** 3), 2),
            "available_gb": round(mem.available / (1024 ** 3), 2),
            "percent": mem.percent,
        }

    @staticmethod
    def get_process_count() -> int:
        """Ermittelt die Anzahl der laufenden Prozesse.

        Returns:
            Anzahl der aktiven Prozesse.
        """
        return len(psutil.pids())

    @staticmethod
    def get_logged_users() -> List[Dict[str, str]]:
        """Ermittelt die aktuell eingeloggten Nutzer.

        Returns:
            Liste von Dicts mit name, terminal und host.
        """
        users = psutil.users()
        return [
            {
                "name": user.name,
                "terminal": user.terminal or "N/A",
                "host": user.host or "local",
            }
            for user in users
        ]

    def get_all_metrics(self, disk_path: str = "/") -> Dict:
        """Erfasst alle Systemmetriken auf einmal.

        Args:
            disk_path: Pfad des zu prüfenden Dateisystems.

        Returns:
            Dict mit allen Metriken.
        """
        return {
            "disk": self.get_disk_usage(disk_path),
            "ram": self.get_ram_usage(),
            "processes": self.get_process_count(),
            "users": self.get_logged_users(),
        }

    @staticmethod
    def format_output(metrics: Dict) -> str:
        """Formatiert die Metriken für die Konsolenausgabe.

        Args:
            metrics: Dict aus get_all_metrics().

        Returns:
            Formatierter String.
        """
        lines = [
            "=" * 50,
            "SYSTEM MONITORING REPORT",
            "=" * 50,
            "",
            "--- Festplatte ---",
            f"  Gesamt:     {metrics['disk']['total_gb']} GB",
            f"  Belegt:     {metrics['disk']['used_gb']} GB",
            f"  Frei:       {metrics['disk']['free_gb']} GB",
            f"  Auslastung: {metrics['disk']['percent']}%",
            "",
            "--- Arbeitsspeicher ---",
            f"  Gesamt:     {metrics['ram']['total_gb']} GB",
            f"  Belegt:     {metrics['ram']['used_gb']} GB",
            f"  Verfügbar:  {metrics['ram']['available_gb']} GB",
            f"  Auslastung: {metrics['ram']['percent']}%",
            "",
            f"--- Prozesse: {metrics['processes']} ---",
            "",
            "--- Eingeloggte Nutzer ---",
        ]

        if metrics["users"]:
            for user in metrics["users"]:
                lines.append(
                    f"  {user['name']} "
                    f"(Terminal: {user['terminal']}, "
                    f"Host: {user['host']})"
                )
        else:
            lines.append("  Keine Nutzer eingeloggt.")

        lines.append("=" * 50)
        return "\n".join(lines)
