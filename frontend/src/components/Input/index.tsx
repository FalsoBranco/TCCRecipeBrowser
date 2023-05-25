import React from 'react';
import {
  FormControl,
  Input as NativeBaseInput,
  IInputProps,
} from 'native-base';

interface InputProps extends IInputProps {
  labelName?: string | null;
  errorMessage?: string | null;
}

const CustomInput = ({
  errorMessage = null,
  labelName = null,
  isInvalid,
  ...rest
}: InputProps) => {
  const invalid = !!errorMessage || isInvalid;
  return (
    <FormControl mb={4} isInvalid={invalid}>
      {labelName ? (
        <FormControl.Label
          _text={{
            color: 'black',
          }}
        >
          {labelName}
        </FormControl.Label>
      ) : null}
      <NativeBaseInput
        size="xl"
        isInvalid={invalid}
        color="dark.400"
        _invalid={{
          borderWidth: '2',
          borderColor: 'red.600',
        }}
        {...rest}
      />

      <FormControl.ErrorMessage>{errorMessage}</FormControl.ErrorMessage>
    </FormControl>
  );
};

export default CustomInput;
