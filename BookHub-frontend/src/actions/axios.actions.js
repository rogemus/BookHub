import axios from 'axios';
import {
	ERRORS
} from './types';

const API_URL = '/api';

const instance = axios.create({
	baseURL: API_URL,
	headers: {
		accept: 'application/json'
	}
});

export function _get(path, config, type) {
	return (dispatch) => {
		instance.get(`/${path}/`, {params: config})
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
