function login () {
    swal.withForm({
        title: 'You can login with:',
        showCancelButton: true,
        confirmButtonColor: '#DD6B55',
        confirmButtonText: 'SIGN IN',
        cancelButtonText: 'CANCEL',
        closeOnConfirm: false,
        imageUrl: "http://t4t5.github.io/sweetalert/example/images/thumbs-up.jpg",
        formFields: [
            { id: 'weibo', value: 'login with weibo', type: 'button'},
            { id: 'google', value: 'login with google', type: 'button'},
            { id: 'facebook', value: 'login with facebook', type: 'button'},
            { name: 'OR', value: 'OR', type: 'text' },
            { id: 'name', placeholder: 'Username', type: 'input' },
            { id: 'psw', placeholder: 'Password', type: 'password' }
        ]
    }, function(isConfirm) {
        // do whatever you want with the form data
        console.log(this.swalForm); // { name: 'user name', nickname: 'what the user sends' }
        if (isConfirm){
            swal("Confirm", this.swalForm.name, "success");
        }
    });
}
