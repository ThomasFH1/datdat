all:
	@clear
	@rm -rf "./Theatre.db"
	@cat prosjekt_del_1/opprett.sql prosjekt_del_1/schema.sql prosjekt_del_1/queries.sql | sqlite3
	@cat prosjekt_del_2/insert-db.sql | sqlite3 Theatre.db
	#@python3 her skal populate.py kjøres
	@cat prosjekt_del_1/queries.sql | sqlite3 Theatre.db
