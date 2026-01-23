# MMOS Aruba app

L'app `mmos_aruba` definisce i DocType e le API necessarie per gestire Aruba Cloud (VPS, WireGuard, Load Balancer) da Press.

## Componenti principali
- **MMOS Aruba Account**: registra endpoint, API key e stato dell'account Aruba. Viene creato un record `placeholder` automaticamente.
- **MMOS Aruba Node**: rappresenta un servizio Aruba con IP, service_id, ruolo e stato; il campo `last_sync` viene aggiornato dai job di sincronizzazione.
- **API**: `mmos_aruba.api.sync.get_nodes_summary` restituisce conteggi per stato; `update_node_status` aggiorna lo stato di un nodo.

## Installazione
```bash
cd /tmp/zfsv3/nvme11/_michelemilazzo/data/mmos-dev
bench get-app ./apps/mmos_aruba
bench --site dev.onekeyco.com install-app mmos_aruba
bench --site dev.onekeyco.com migrate
```

## Sincronizzazione
1. Usa Aruba CLI/API per interrogare l'inventario (es. `aruba-cloud compute server list`).
2. Mappa i risultati su `MMOS Aruba Node` e chiama `frappe.db.set_value` per aggiornare `last_sync`.
3. Chiama `frappe.call("mmos_aruba.api.sync.get_nodes_summary")` per esporre il riepilogo a dashboard esterni.

## Espansioni consigliate
- Aggiungi un job scheduler che esegue `bench execute mmos_aruba.api.sync.sync_nodes` e che scrive `state`/`last_sync` per ogni nodo.
- Integra con WireGuard Manager (es. collegando `MMOS Aruba Node` a `MMOS Node` e `Health Check`).
