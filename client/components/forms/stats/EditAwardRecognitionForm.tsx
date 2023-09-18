import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import useAxios from '@/lib/utils/axios';
import { useForm, SubmitHandler } from 'react-hook-form';
import { AwardRecognitionInputs } from './NewAwardRecognitionForm';

// wip
const EditAwardRecognitionForm = ({
  id,
  closeModal,
}: {
  id: string;
  closeModal: any;
}) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<AwardRecognitionInputs>();
  const api = useAxios();

  const onSubmit: SubmitHandler<AwardRecognitionInputs> = async (data) => {
    try {
      console.log(data);
      const response = await api.patch(`/awards-recognition-stats/${id}`, data);
      console.log('response', response);
      return response;
    } catch (error) {
      console.error('error', error);
    }
  };
  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      <Form.Group className="mb-3" controlId="formYTDStatQuarter">
        <Form.Label>Quarter</Form.Label>
        <Form.Control type="text" placeholder="Q3" {...register('quarter')} />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formYTDStatCompany">
        <Form.Label>Company</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Company"
          {...register('company')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formYTDStatTitle">
        <Form.Label>Title</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Title"
          {...register('title')}
        />
      </Form.Group>
      <div className="mt-4">
        <Button variant="primary" type="submit">
          Submit
        </Button>
        <Button variant="light" onClick={closeModal}>
          Cancel
        </Button>
      </div>
    </Form>
  );
};

export default EditAwardRecognitionForm;
