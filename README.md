# MMOS Aruba

`mmos_aruba` è un'app Frappe/Press che centralizza l'inventario e le policy Aruba Cloud (Geek, Enterprise, VPS). Permette di memorizzare account, servizi attivi, configurazioni di rete e di esporre API per sincronizzare i nodi con Press.

## Caratteristiche
- `MMOS Aruba Account`: memo delle credenziali Aruba (API key, endpoint, stato, note).
- `MMOS Aruba Node`: rappresenta un VPS/servizio Aruba, con IP pubblico, ruolo operativo, timestamp di sincronizzazione e link all'account.
- API whitelisted per ottenere riepiloghi e aggiornare lo stato dei nodi da automation.
- `after_install` crea un account di placeholder per evitare installazioni vuote.

## Installazione su Press bench
```bash
cd /tmp/zfsv3/nvme11/_michelemilazzo/data/mmos-dev
bench get-app ./apps/mmos_aruba
bench --site dev.onekeyco.com install-app mmos_aruba
bench --site dev.onekeyco.com migrate
```

## Uso operativo
1. Inserisci gli account Aruba (API key + endpoint). Proteggi le credenziali con permessi `System Manager`.
2. Registra i servizi (VPS, load balancer) collegandoli all'account e definendo `role` (`gateway`, `storage`, `wireguard`) e `state`.
3. Scrivi job Frappe che chiamano `mmos_aruba.api.sync.sync_nodes()` per aggiornare `last_sync` e `state` automatico.

## Esportazione configurazioni
Aggiungi le API Aruba CLI (per es. `aruba-cloud`) nel tuo job di sincronizzazione e mappa le risposte sui DocType. Garantisci la revisione delle chiavi prima di salvare i record.
