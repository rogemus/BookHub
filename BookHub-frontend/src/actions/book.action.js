import axios from 'axios';
import {GET_BOOK} from './types';

const API_URL = 'http://localhost:8080/api';

export function getBook(bookID) {
	const config = {
		path: `books/${bookID}`,
		type: GET_BOOK
	};

	return _get(config.path, config.params, config.type);
}

function _get(path, params, type) {
	return (dispatch) => {
		axios.get(`${API_URL}/${path}`, params)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: type
				});
			});
	};
}
