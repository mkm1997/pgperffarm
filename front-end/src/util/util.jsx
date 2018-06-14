const BASE_URL = '127.0.0.1:8000'
class PGUtil {
    request(param) {
        return new Promise((resolve, reject) => {
            $.ajax({
                type: param.type || 'get',
                url: param.url || '',
                dataType: param.dataType || 'json',
                data: param.data || null,
                success: res => {
                    // request success

                    typeof resolve === 'function' && resolve(res, res.msg);
                    // if (0 === res.status) {
                    //     typeof resolve === 'function' && resolve(res.data, res.msg);
                    // }
                    // // nologin force to login
                    // else if (10 === res.status) {
                    //     this.doLogin();
                    // }
                    // else {
                    //     typeof reject === 'function' && reject(res.msg || res.data);
                    // }
                },
                error: err => {
                    typeof reject === 'function' && reject(err.statusText);
                }
            });
        });
    }

    // success tips
    successTips(successMsg) {
        alert(successMsg);
    }

    // error tips
    errorTips(errMsg) {
        alert(errMsg);
    }

    // set local storage
    setStorage(name, data) {
        let dataType = typeof data;
        // json obj
        if (dataType === 'object') {
            window.localStorage.setItem(name, JSON.stringify(data));
        }
        // basical type
        else if (['number', 'string', 'boolean'].indexOf(dataType) >= 0) {
            window.localStorage.setItem(name, data);
        }
        // other unacceptable type
        else {
            alert('type unacceptabled');
        }
    }

    // get local storage
    getStorage(name) {
        let data = window.localStorage.getItem(name);
        if (data) {
            return JSON.parse(data);
        }
        else {
            return '';
        }
    }

    // remove local storage
    removeStorage(name) {
        window.localStorage.removeItem(name);
    }
}

export default PGUtil;