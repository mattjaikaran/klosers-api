import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import useAxios from '@/lib/utils/axios';
import { useForm, SubmitHandler } from 'react-hook-form';

export interface YTDStatInputs {
  quarter: string;
  company: string;
  title: string;
  market: string;
  percent_quota_attainment: string;
  avg_deal_size: string;
  avg_sales_cycle: string;
  industry?: string;
  leaderboard_rank?: string;
}

const NewYTDStatForm = ({ closeModal }: { closeModal: any }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<YTDStatInputs>();
  const api = useAxios();

  const onSubmit: SubmitHandler<YTDStatInputs> = async (data) => {
    try {
      console.log(data);
      const ytdStat = {
        quarter: data.quarter,
        company: data.company,
        title: data.title,
        market: data.market,
        percent_quota_attainment: data.percent_quota_attainment,
        avg_deal_size: data.avg_deal_size,
        avg_sales_cycle: data.avg_sales_cycle,
        industry: data.industry,
        leaderboard_rank: data.leaderboard_rank,
      };
      console.log('ytdStat', ytdStat);
      const response = await api.post('/ytd-stats', ytdStat);
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
      <Form.Group className="mb-3" controlId="formYTDStatMarket">
        <Form.Label>Market</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Market Type"
          {...register('market')}
        />
      </Form.Group>
      <Form.Group
        className="mb-3"
        controlId="formYTDStatpercentQuotaAttainment"
      >
        <Form.Label>Percent Quota Attainment</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter % Quota Attainment"
          {...register('percent_quota_attainment')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formYTDStatAvgDealSize">
        <Form.Label>Avg Deal Size</Form.Label>
        <Form.Control
          type="text"
          placeholder="Avg Deal Size"
          {...register('avg_deal_size')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formYTDStatIndustry">
        <Form.Label>Industry</Form.Label>
        <Form.Control
          type="text"
          placeholder="Industry"
          {...register('industry')}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formYTDStatLeaderboardRank">
        <Form.Label>Leaderboard Rank</Form.Label>
        <Form.Control
          type="text"
          placeholder="#2"
          {...register('leaderboard_rank')}
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

export default NewYTDStatForm;
