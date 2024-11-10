const BASE_URL = 'http://localhost:8000/';

const getHeaders = () => {
  // const APP_KEY = 'some_key';

  // const getToken = () => {
  //   const userData = null; // get data from store
  //   // return userData?.authToken || null;
  // };

  // return {
  //   'Content-Type': 'application/json',
  //   Authorization: `Bearer ${getToken()}`,
  //   'X-App-Key': APP_KEY,
  // };

  return {
    'Content-Type': 'application/json',
  };
};

type Method = 'GET' | 'POST' | 'PUT' | 'DELETE';

class ApiMethods {
  static apiRequest<T extends object>(
    method: Method,
    url: string,
    body = undefined
  ) {
    url = BASE_URL + url;
    return new Promise<T>((resolve, reject) => {
      fetch(url, { method, body: JSON.stringify(body), headers: getHeaders() })
        .then((res) => res.json())
        .then(resolve)
        .catch(reject);
    });
  }

  static get<T extends object>(url: string) {
    return this.apiRequest<T>('GET', url);
  }

  static post(url: string, body: object) {
    return this.apiRequest('POST', url, body);
  }

  static put(url: string, body: object) {
    return this.apiRequest('PUT', url, body);
  }

  static delete(url: string) {
    return this.apiRequest('DELETE', url);
  }
}

export default ApiMethods;