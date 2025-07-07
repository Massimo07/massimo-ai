"""
Modulo: run_bot.py
Entrypoint rapido per avviare Massimo AI come servizio (importa main.py o altri launcher).
Pronto per hosting cloud, Docker, process manager, serverless.
"""

import main

if __name__ == "__main__":
    main.main()
