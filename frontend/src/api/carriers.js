import axios from 'axios'
import { resolve } from 'path';
import { rejects } from 'assert';

export default {
    fetchCarriers(method, params, data) {
        if(method === 'post'){
            return ajax('api/carriers/', method, {data})
        }else {
            return ajax('api/carriers/','get', null, null)
        }
    }
}

/**
 * @param url
 * @param method
 * @param params
 * @param data
 * @returns 
 */

function ajax(url, method, options){
    if(options !== undefined){
        var {params={}, data={}} = options
    } else {
        params = data = {}
    }
    return new Promise((resolve, rejects) => {
        axios({
            url,
            method,
            params,
            data
        }).then(res=>{
            resolve(res)
        }, res => {
            rejects(res)
        })
    })
}