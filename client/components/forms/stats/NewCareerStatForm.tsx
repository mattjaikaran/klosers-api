import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import useAxios from '@/lib/utils/axios';
import { useForm, SubmitHandler } from 'react-hook-form';

export interface CareerStatInputs {
  year: string;
  company: string;
  title: string;
  market: string;
  percentQuotaAttainment: string;
  avgDealSize: string;
  avgSalesCycle: string;
  industry?: string;
  leaderboardRank?: string;
}

const NewCareerStatForm = ({ closeModal }: { closeModal: any }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CareerStatInputs>();
  const api = useAxios();

  const onSubmit: SubmitHandler<CareerStatInputs> = async (data) => {
    try {
      console.log(data);
      // const response = await api.post('/career-stat', data);
      // console.log('response', response);
      // return response;
    } catch (error) {
      console.error('error', error);
    }
  };
  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      <Form.Group className="mb-3" controlId="formCareerStatQuarter">
        <Form.Label>Year</Form.Label>
        <Form.Control type="text" placeholder="Q3" {...register('year')} />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formCareerStatCompany">
        <Form.Label>Company</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Company"
          {...register('company')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formCareerStatTitle">
        <Form.Label>Title</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Title"
          {...register('title')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formCareerStatMarket">
        <Form.Label>Market</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Market Type"
          {...register('market')}
        />
      </Form.Group>
      <Form.Group
        className="mb-3"
        controlId="formCareerStatpercentQuotaAttainment"
      >
        <Form.Label>Percent Quota Attainment</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter % Quota Attainment"
          {...register('percentQuotaAttainment')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formCareerStatAvgDealSize">
        <Form.Label>Avg Deal Size</Form.Label>
        <Form.Control
          type="text"
          placeholder="Avg Deal Size"
          {...register('avgDealSize')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formCareerStatIndustry">
        <Form.Label>Industry</Form.Label>
        <Form.Control
          type="text"
          placeholder="Industry"
          {...register('industry')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formCareerStatLeaderboardRank">
        <Form.Label>Leaderboard Rank</Form.Label>
        <Form.Control
          type="text"
          placeholder="#2"
          {...register('leaderboardRank')}
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

export default NewCareerStatForm;