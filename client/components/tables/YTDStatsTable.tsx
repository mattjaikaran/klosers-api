import { useState } from 'react';
import Table from 'react-bootstrap/Table';
import Alert from 'react-bootstrap/Alert';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import NewYTDStatForm from '../forms/stats/NewYTDStatForm';
import EditYTDStatForm from '../forms/stats/EditYTDStatForm';

export interface YTDStatsInputs {
  quarter: string;
  company: string;
  title: string;
  market: string;
  percentQuotaAttainment: string;
  avgDealSize: string;
  avgSalesCycle: string;
  industry?: string;
  leaderboardRank?: string;
}

const YTDStatsTable = ({ data }: { data: any }) => {
  const [show, setShow] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [message, setMessage] = useState(false);

  // Add modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  // Edit modal
  const handleCloseEditModal = () => setShowEditModal(false);
  const handleShowEditModal = () => setShowEditModal(true);

  return (
    <>
      <Table responsive>
        <thead>
          <tr>
            <th>Quota Verified</th>
            <th>Quarter</th>
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
              <td>{item.quarter}</td>
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
        Add YTD Stat
      </Button>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add YTD Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {message ? <Alert variant="danger">{message}</Alert> : null}
          <NewYTDStatForm closeModal={handleClose} />
        </Modal.Body>
      </Modal>
      <Modal show={showEditModal} onHide={handleCloseEditModal}>
        <Modal.Header closeButton>
          <Modal.Title>Edit YTD Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {message ? <Alert variant="danger">{message}</Alert> : null}
          <EditYTDStatForm id={'13'} closeModal={handleCloseEditModal} />
        </Modal.Body>
      </Modal>
    </>
  );
};
export default YTDStatsTable;