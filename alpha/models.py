from django.db import models

class Data(models.Model):
    exchange_rate = models.FloatField()
    last_refreshed = models.CharField(max_length=100)
    bid_price = models.FloatField()
    ask_price = models.FloatField()
    created_at = models.DateTimeField( auto_now_add = True )
    
    def __str__(self) -> str:
        return f"Exchange Rate {self.last_refreshed}"