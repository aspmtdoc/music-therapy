from django.conf.urls import url

from musictherapy import views
import django.contrib.auth.views as auth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musictherapy/patients/$', views.patients, name='list'),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_comassess/$', views.save_com_assess, name="save_commassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_comgoals/$', views.save_com_goals, name="save_comgoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_pssassess/$', views.save_pss_assess, name="save_pssassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_pssgoals/$', views.save_pss_goals, name="save_pssgoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_motorassess/$', views.save_motor_assess, name="save_motorassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_motorgoals/$', views.save_motor_goals, name="save_motorgoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_cogassess/$', views.save_cog_assess, name="save_cogassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_coggoals/$', views.save_cog_goals, name="save_coggoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_socialassess/$', views.save_social_assess, name="save_socialassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_socialgoals/$', views.save_social_goals, name="save_socialgoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_musicassess/$', views.save_music_assess, name="save_musicassessment"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_musicgoals/$', views.save_music_goals, name="save_musicgoals"),
    url(r'^musictherapy/(?P<user_id>[0-9]+)/submit_goals/$', views.save_user_goals, name="save_goals"),
    url(r'^musictherapy/new/$', views.create_user, name='create_user'),
    url(r'^musictherapy/staff/$', views.create_staff, name='create_staff'),
    url(r'^musictherapy/new/submit_userinfo/$', views.save_new_basic, name='new_userinfo'),
    url(r'^musictherapy/login/$', auth.login, {
        'template_name': 'musictherapy/index.html'
    }, name='login'),
    url(r'^musictherapy/logout/$', auth.logout, {
        'next_page': '/musictherapy'
    }, name='logout'),
    url(r'^musictherapy/change_password/$', auth.password_change, {
            'template_name': 'musictherapy/change_password.html',
            'post_change_redirect': '/musictherapy/patients?status=pass_change_success',
    }, name="password_change"),
]

