import React from 'react';
import {
	Form,
	Button
} from 'semantic-ui-react';

export default (props) => {
	return (
		<Form onSubmit={props.handleSubmit}>
			<Form.Field required>
				<label>Email</label>
				<input
					placeholder='Email'
					required
					value={props.values.email}
					onChange={props.handleChange}
					name='email'
					type='email'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Password</label>
				<input
					placeholder='Password'
					required
					onChange={props.handleChange}
					value={props.values.password}
					name='password'
					type="password"
				/>
			</Form.Field>
			<Button type='submit' primary>Submit</Button>
		</Form>
	);
};
