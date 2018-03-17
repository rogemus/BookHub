import axios from 'axios';
import {
	ERRORS
} from './types';

const API_URL = 'http://localhost:8080/api';

const instance = axios.create({
	baseURL: API_URL,
	headers: {
		'Accept': 'application/json'
	}
});

export function _get(path, config, type) {
	return (dispatch) => {
		instance.get(`/${path}/`, config)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: type
				});
			})
			.catch((error) => {
				dispatch({
					payload: error,
					type: ERRORS
				});
			});
	};
}
