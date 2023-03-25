class UserUseCases:
    def __init__(self):
        self.session = 'repository.connection'
    
    async def create_user(self):
        # TODO: verificar se usuario ja existe
        # TODO: se nao existir incluir no banco
        pass
        
