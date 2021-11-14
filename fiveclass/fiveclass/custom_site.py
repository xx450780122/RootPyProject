from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_head = '后代管理'
    site_title='hao'
    index_title='首页'

customsite = CustomSite(name= 'cus_admin')
