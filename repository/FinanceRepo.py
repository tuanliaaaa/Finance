class FinanceRepo(BaseRepo):
    def add_finance(self, finance_id: int, name: str, description: str, price: float, start_at: str, end_at: str):
        finance = {
            'id': finance_id,
            'name': name,
            'description': description,
            'price': price,
            'startAt': start_at,
            'endAt': end_at
        }
        self.add(finance)

    def update_finance(self, finance_id: int, name: str = None, description: str = None, price: float = None, start_at: str = None, end_at: str = None):
        updates = {}
        if name is not None:
            updates['name'] = name
        if description is not None:
            updates['description'] = description
        if price is not None:
            updates['price'] = price
        if start_at is not None:
            updates['startAt'] = start_at
        if end_at is not None:
            updates['endAt'] = end_at

        self.update('id', finance_id, updates)

    def delete_finance(self, finance_id: int):
        self.delete('id', finance_id)
