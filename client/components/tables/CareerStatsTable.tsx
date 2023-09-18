import { useState } from 'react';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import useAxios from '@/lib/utils/axios';
import { useForm, SubmitHandler } from 'react-hook-form';
import NewCareerStatForm from '../forms/stats/NewCareerStatForm';
import EditCareerStatForm from '../forms/stats/EditCareerStatForm';

interface CareerStatsInputs {
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

const CareerStatsTable = ({ data }: { data: any }) => {
  const [show, setShow] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);

  // Add modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  // Edit modal
  const handleCloseEditModal = () => setShowEditModal(false);
  const handleShowEditModal = () => setShowEditModal(true);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CareerStatsInputs>();
  const api = useAxios();

  const onSubmit: SubmitHandler<CareerStatsInputs> = async (data) => {
    try {
      console.log(data);
      // const response = await api.post('/login', data);
      // console.log('response', response);
      // return response;
    } catch (error) {
      console.error('error', error);
    }
  };
  return (
    <>
      <Table responsive striped>
        <thead>
          <tr>
            <th>Quota Verified</th>
            <th>Year</th>
            <th>Company</th>
            <th>Title</th>
            <th>Market</th>
            <th>% Quota Attainment</th>
            <th>Avg Deal Size</th>
            <th>Avg Sales Cycle</th>
            <th>Industry</th>
            <th>Leaderboard Rank</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item: any) => (
            <tr key={item.id}>
              <td>{item.quota_verified ? 'Verified' : '-'}</td>
              <td>{item.year}</td>
              <td>{item.company}</td>
              <td>{item.title}</td>
              <td>{item.market}</td>
              <td>{item.quota_attainment_percent}</td>
              <td>{item.avg_deal_size}</td>
              <td>{item.avg_sales_cycle}</td>
              <td>{item.industry}</td>
              <td>{item.leaderboard_rank}</td>
              <td>
                <Button variant="outline-success" onClick={handleShowEditModal}>
                  Edit
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
      <Button className="my-3" variant="outline-primary" onClick={handleShow}>
        Add Year
      </Button>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add Career Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <NewCareerStatForm closeModal={handleClose} />
        </Modal.Body>
      </Modal>
      <Modal show={showEditModal} onHide={handleCloseEditModal}>
        <Modal.Header closeButton>
          <Modal.Title>Edit Career Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <EditCareerStatForm id={'123'} closeModal={handleCloseEditModal} />
        </Modal.Body>
      </Modal>
    </>
  );
};
export default CareerStatsTable;