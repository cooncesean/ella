
from south.db import db
from django.db import models
from ella.photos.models import *

class Migration:
    
    def forwards(self, orm):
        db.execute('''UPDATE photos.formatedphoto SET image = filename''')
    
    
    def backwards(self, orm):
        db.execute('''UPDATE photos.formatedphoto SET filename = image''')
    
