# Paso 1. Componente base y notificación concreta:
class Notifier:
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Email] {message}")


# Paso 2. Decoradores que envuelven a otro Notifier:
class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)


class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[SMS] {message}")


class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[Slack] {message}")


# Paso 3. Componer en tiempo de ejecución:
notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
notifier.send("Servidor caído")
