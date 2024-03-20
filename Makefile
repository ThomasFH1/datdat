all:
	@clear
	@rm -rf "./Theatre.db"
	@echo "Starter script..."
	@cat prosjekt_del_1/opprett.sql prosjekt_del_1/schema.sql | sqlite3
	@echo "Opprettet tabell."
	@cat prosjekt_del_2/insert-db.sql | sqlite3 Theatre.db
	@echo "Fylt inn"
	@echo "Database opprettet og fylt med data."
	@cat prosjekt_del_1/queries.sql | sqlite3 Theatre.db
