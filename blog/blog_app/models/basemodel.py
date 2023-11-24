from uuid import uuid4
from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    """Base model for all models"""
    id = models.CharField(primary_key=True, max_length=200, unique=True, blank=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid4())
        if not self.created_at:
            self.created_at = datetime.utcnow()
        if not self.updated_at:
            self.updated_at = datetime.utcnow()

    def save(self, *args, **kwargs):
        """Method to save the instance to db"""
        self.updated_at = datetime.utcnow()
        super().save(*args, **kwargs)

    def to_dict(self):
        """Method to return a dictionary representation of the instance"""
        dict_rep = self.__dict__.copy()
        dict_rep.pop('_state', None)
        dict_rep.update({'__class__': self.__class__.__name__})
        if dict_rep.get('created_at'):
            dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        if dict_rep.get('updated_at'):
            dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()
        return dict_rep
    
    class Meta:
        """Meta class for BaseModel"""
        abstract = True