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

export function _get(path, config, actionType) {
	return (dispatch) => {
		instance.get(`/${path}/`, config)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: actionType
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

export function _post(path, config, actionType) {
	return (dispatch) => {
		instance.post(`/${path}/`, config)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: actionType
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
