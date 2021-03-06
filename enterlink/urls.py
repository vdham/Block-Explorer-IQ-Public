from django.conf.urls import url, include
from enterlink import views, edit
from django.contrib.auth import views as django_views
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

# THIS LANGUAGE SETTING WORKS WHEN THE SETTINGS IS FORCED TO LANGUAGE_CODE = 'zh-hans'
# FOR SOME REASON, jsi18n IS NOT LANGUAGE AWARE
# jsi18n has an issue with Chinese since it is zh-hans. It works for ko and other two-character languages

urlpatterns = [
	url(ur'^$', views.index, name='index'),
	url(ur'^(?i)brainpower/(?P<account_name>(.*))/$', views.brainpowermgmt, name='brainpowermgmt'),
	url(ur'^(?i)rewards/(?P<account_name>(.*))/$', views.rewardsmgmt, name='rewardsmgmt'),
	url(ur'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
	url(ur'^(?i)contact/$', views.contact, name='contact'),
	url(ur'^(?i)leadership/$', TemplateView.as_view(template_name="enterlink/leadership.html"), name='leadership'),
	url(ur'^(?i)exchange-listings/$', TemplateView.as_view(template_name="enterlink/exchange-listings.html"), name='exchange_listings'),
	url(ur'^(?i)transfer-iq/$', TemplateView.as_view(template_name="enterlink/transfer-iq.html"), name='transfer_iq'),
	url(ur'^(?i)editing-disabled/$', TemplateView.as_view(template_name="enterlink/editing-disabled.html"), name='editing_disabled'),
	url(ur'^(?i)recent-activity/$', views.recent_activity, name='recent_activity'),
	url(ur'^(?i)create_page/$', edit.create_page, name='create_page'),
	url(ur'^(?i)dropzone/$', views.dropzone, name='dropzone'),
	url(ur'^(?i)test_page/$', views.test_page, name='test_page'),
	url(ur'^(?i)error/$', views.error, name='error'),
	url(ur'^(?i)error404/$', TemplateView.as_view(template_name="enterlink/error.html"), name='error404'),
	url(ur'^(?i)cachefinalizedresult/(?P<proposal_id>(.*))/$', edit.cacheFinalizedResult, name='cacheFinalizedResult'),
	url(ur'^(?i)hoverblurb/(?P<url_param>(.*))/$', views.hoverBlurb, name='hoverBlurb'),
	url(ur'^(?i)language-selector/$', views.language_selector, name='language_selector'),
	url(ur'^(?i)search/$', views.search, name='search'),
	url(ur'^(?i)search/iframe/$', views.searchiframe, name='searchiframe'),
	url(ur'^favicon.ico/$', views.favicon, name='favicon'),
	url(ur'^robots\.txt$', TemplateView.as_view(template_name='enterlink/robots.txt', content_type='text/plain')),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Add_New_Infobox/$', edit.AJAX_Add_New_Infobox, name='AJAX_Add_New_Infobox'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Add_New_Link/$', edit.AJAX_Add_New_Link, name='AJAX_Add_New_Link'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Check_Blurb/$', views.AJAX_Check_Blurb, name='AJAX_Check_Blurb'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Fetch_Blurb_Compare/(?P<new_ipfs>(.*))/(?P<old_ipfs>(.*))/$', edit.AJAX_Fetch_Blurb_Compare, name='AJAX_Fetch_Blurb_Compare'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Fetch_New_Infobox_Form/(?P<url_param>(.*))/$', edit.AJAX_Fetch_New_Infobox_Form, name='AJAX_Fetch_New_Infobox_Form'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Fetch_Page_Photo/(?P<url_param>(.*))/$', edit.AJAX_Fetch_Page_Photo, name='AJAX_Fetch_Page_Photo'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Hoverblurb/(?P<url_param>(.*))/$', views.AJAX_Hoverblurb, name='AJAX_Hoverblurb'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Hoverlink/(?P<url_param>(.*))/$', views.AJAX_Hoverlink, name='AJAX_Hoverlink'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_QR_Code_Iframe/(?P<inputslug>(.*))/$', views.AJAX_QR_Code_Iframe, name='AJAX_QR_Code_Iframe'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Picture_Upload/(?P<photo_type>(.*))/(?P<identifier>(.*))/$', edit.AJAX_Picture_Upload, name='AJAX_Picture_Upload'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Schema_Search/$', views.AJAX_Schema_Search, name='AJAX_Schema_Search'),
	url(ur'^(?i)AJAX-REQUEST/AJAX_Search/(?P<url_param>(.*))/$', views.AJAX_Search, name='AJAX_Search'),
	url(ur'^(?i)pagecounter/(?P<page_slug>(.*))/$', views.pagecounter, name='pagecounter'),
	url(ur'^(?i)accounts/passwordreset/$', django_views.password_change, {'template_name' : 'admin/password_change_form.html'}, name='password_change'),
    url(ur'^(?i)account/reset/done/$', django_views.password_reset_done, name='password_reset_done'),
    url(ur'^(?i)account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', django_views.password_reset_confirm, name='password_reset_confirm'),
    url(ur'^(?i)account/done/$', django_views.password_reset_complete, name='password_reset_complete'),
	url(ur'^(?i)account/reset/$', django_views.password_reset, name='password_reset'),
	url(ur'^(?i)wiki/(?P<url_param>(.*))/advanced_edit/$', edit.edit, name='edit'),
	url(ur'^(?i)vote/(?P<url_param>(.*))/$', edit.vote, name='vote'),
	url(ur'^(?i)sync_to_chain/$', edit.sync_to_chain, name='sync_to_chain'),
	url(ur'^(?i)check_new_articles/$', edit.check_new_articles, name='check_new_articles'),
	url(ur'^(?i)save_draft/$', edit.save_draft, name='save_draft'),
	url(ur'^(?i)get_draft/$', edit.get_draft, name='edit_draft'),
	url(ur'^(?i)wiki/(?P<url_param>(.*))/amp/$', views.template_handler_blockchain, name='template_handler_blockchain'),
	url(ur'^(?i)wiki/(?P<url_param>(.*))/$', views.template_handler_blockchain, name='template_handler_blockchain'),
	url(ur'^(?P<url_param>(.*))/advanced_edit/$', views.edit_301, name='edit_301'),
	url(ur'^(?P<url_param>(.*))/amp/$', views.template_handler_301_amp, name='template_handler_301_amp'),
	url(ur'^(?P<url_param>(.*))/$', views.template_handler_301, name='template_handler_301'),

]
