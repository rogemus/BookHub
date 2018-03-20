import React from 'react';
import {Form,Button} from 'semantic-ui-react';

export default (props) => {
	return(
		<Form onSubmit={props.handleSubmit}>
			<Form.Field>
				<label>Imię</label>
				<input 
					placeholder='Email'
					value={props.values.name}
					onChange={props.handleChange}
					name='name'
					type='string'
				/>
			</Form.Field>
			<Form.Field>
				<label>Surname</label>
				<input 
					placeholder='Surname'
					value={props.values.surname}
					onChange={props.handleChange}
					name='surname'
					type='string'
				/>
			</Form.Field>
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