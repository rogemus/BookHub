import React from 'react';
import PropTypes from 'prop-types';

export default function RegisterForm(props) {
	return (
		<form onSubmit={props.handleSubmit} className="form">
			<div className='form-field'>
				<label htmlFor='username'>Username</label>
				<input
					id='username'
					placeholder='Username'
					value={props.values.username}
					onChange={props.handleChange}
					name='username'
					type='text'
					required
				/>
			</div>
			<div className='form-field'>
				<label htmlFor='first_name'>Name</label>
				<input
					id='first_name'
					placeholder='First Name'
					value={props.values.first_name}
					onChange={props.handleChange}
					name='first_name'
					required
					type='text'
				/>
			</div>
			<div className='form-field'>
				<label htmlFor="last_name">Surname</label>
				<input
					id='last_name'
					placeholder='Last Name'
					value={props.values.last_name}
					onChange={props.handleChange}
					name='last_name'
					required
					type='text'
				/>
			</div>
			<div className='form-field'>
				<label htmlFor='email'>Email</label>
				<input
					placeholder='Email'
					required
					value={props.values.email}
					onChange={props.handleChange}
					name='email'
					type='email'
					id='email'
				/>
			</div>
			<div className='form-field'>
				<label htmlFor='password'>Password</label>
				<input
					id='password'
					placeholder='Password'
					required
					onChange={props.handleChange}
					value={props.values.password}
					name='password'
					type="password"
				/>
			</div>
			<button type='submit' className="btn">Submit</button>
		</form>
	);
}

RegisterForm.propTypes = {
	handleSubmit: PropTypes.func,
	handleChange: PropTypes.func,
	values: PropTypes.object
};
