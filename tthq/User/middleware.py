class GetPathMiddleware():
    def process_view(self,request,view_func,view_args,view_kwargs):
        #active
        no_urls=[
            # '/User/register/',
            # '/User/register_handle/',
            # '/User/login/',
            # '/User/login_handle/',
            # '/User/logout/',
            # '/User/islogin/',
            # '/User/index/',
            # '/User/user_input/',
            # '/User/detection_name/',
            # '/User/active/',
            # '/User/font/',
            # '/User/logging/',
            # '/User/Verification_code/',
            # '/User/send_sms/',
            # '/User/login_handle/',
            # '/User/font/',
            # '/User/font/',
            # '/admin/',
        ]
        if request.path not in no_urls and 'active' not in request.path:
            request.session['url_path']=request.get_full_path()
